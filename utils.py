from pysnmp.smi import builder, view
import re
from datetime import datetime, timedelta
from pysnmp.hlapi.v3arch.asyncio import *
import time
import os
from enums import COMPILED_MIBS
import cx_Oracle
from mib_compiler import setup_logging


# Cache singleton
_mib_cache = None

# Required MIBs mapping (add as needed)
BRAND_MIB_MAP = ['IF-MIB', 'SNMPv2-MIB','NSCRTV-FTTX-EPON-MIB', 'NSCRTV-FTTX-GPON-MIB', 'V1600D']

# Function to load MIBs
def load_mibs():
    """Load and cache MIBs based on brand; fallback to all if unknown"""
    global _mib_cache
    if _mib_cache:
        return _mib_cache

    print("Loading MIBs...")
    start_time = time.time()

    mib_builder = builder.MibBuilder()

    # Directories
    compiled_mib_dir = COMPILED_MIBS
    if os.path.exists(compiled_mib_dir):
        mib_builder.add_mib_sources(builder.DirMibSource(compiled_mib_dir))
    else:
        raise FileNotFoundError(f"Compiled MIB path not found: {compiled_mib_dir}")

    # Also include source MIBs as fallback if needed
    source_mib_dir = 'mibs'
    if os.path.exists(source_mib_dir):
        mib_builder.add_mib_sources(builder.DirMibSource(source_mib_dir))

    # Choose MIBs to load
    mibs_to_load = BRAND_MIB_MAP

    for mib in mibs_to_load:
        t0 = time.time()
        try:
            mib_builder.load_modules(mib)
            print(f"Loaded {mib} in {time.time() - t0:.2f}s")
        except Exception as e:
            print(f"Warning: Could not load MIB {mib}: {e}")

    _mib_cache = mib_builder
    print(mib_builder.mibSymbols.keys())

    print(f"MIB Load complete in {time.time() - start_time:.2f} seconds.")
    return mib_builder

def parse_onu_device_index(index: int):
    slot = (index >> 25) & 0x7F       # bits 25–31
    pon = (index >> 19) & 0x3F        # bits 19–24
    onu = index & 0x7FFFF             # bits 0–18
    return slot, pon, onu

def format_snmp_output_value(value, value_type):
    """Format the value based on its type"""
    if value_type == "OCTETSTRING":
        # Check if the value is a printable string
        decoded_value = value.prettyPrint()
        if not decoded_value:  
            return '""'
        if not decoded_value.startswith("0x") and all(32 <= ord(char) <= 126 for char in decoded_value):
            return f'STRING: "{decoded_value}"'
        else:
            hex_value = " ".join([f"{byte:02X}" for byte in value.asNumbers()])
            return f'Hex-STRING: {hex_value}'
    elif value_type == "OBJECTIDENTIFIER":
        return f"OID: {value.prettyPrint()}"
    elif value_type == "GAUGE32":
        return f"Gauge32: {value}"
    elif value_type == "COUNTER32":
        return f"Counter32: {value}"
    elif value_type == "COUNTER64":
        return f"Counter64: {value}"
    elif value_type == "TIMETICKS":
        raw_ticks = int(value)
        days = raw_ticks // (24 * 60 * 60 * 100)
        hours = (raw_ticks // (60 * 60 * 100)) % 24
        minutes = (raw_ticks // (60 * 100)) % 60
        seconds = (raw_ticks // 100) % 60
        milliseconds = raw_ticks % 100
        human_readable = f"{days} days, {hours}:{minutes:02}:{seconds:02}.{milliseconds:02}"
        return f"Timeticks: ({raw_ticks}) {human_readable}"
    elif value_type == "IPADDRESS":
        return f"IpAddress: {value.prettyPrint()}"
    elif value_type == "INTEGER":
        return f"INTEGER: {value}"
    elif value_type == "NULL":
        return '""'
    else:
        return f"{value_type}: {value.prettyPrint()}"

# Perform SNMP Walk using async walk_cmd
async def snmp_walk(ip, community, oid, port, snmp_version, snmp_timeout, snmp_retries, debug_mode):
    setup_logging(debug_mode)
    result = []
    # Start timing
    start_time = time.time()
    
    # Load all MIBs
    mib_builder = load_mibs()
    mib_view = view.MibViewController(mib_builder)
    
    # Create the generator for the SNMP walk operation
    objects = walk_cmd(
        SnmpEngine(),
        CommunityData(community, mpModel=snmp_version),
        await UdpTransportTarget.create((ip, port), timeout=snmp_timeout, retries=snmp_retries),
        ContextData(),
        ObjectType(ObjectIdentity(oid)),
        lexicographicMode=False
    )
    
    
    # Process the response from the SNMP walk
    async for errorIndication, errorStatus, errorIndex, varBinds in objects:
        if errorIndication:
            print(f"Error: {errorIndication}")
            return [f"Error: {errorIndication}"]
        elif errorStatus:
            print(f"SNMP Error: {errorStatus.prettyPrint()} at {errorIndex and varBinds[int(errorIndex) - 1][0] or '?'}")
            return [f"SNMP Error: {errorStatus.prettyPrint()} at {errorIndex and varBinds[int(errorIndex) - 1][0] or '?'}"]
        else:
            for varBind in varBinds:
                oid, value = varBind
                
                # Try to resolve to symbolic name
                try:
                    oid_obj = ObjectIdentity(oid)
                    oid_obj.resolve_with_mib(mib_view)
                    symbolic_oid = oid_obj.prettyPrint()
                except Exception as e:
                    # On failure, use the numeric OID but try to resolve as much as possible
                    try:
                        # Try to resolve the module and object name
                        mib_node = mib_view.get_node_name(oid)
                        module_name = mib_node[0]
                        obj_name = mib_node[1]
                        
                        # Get any indices
                        indices = list(oid[len(mib_view.get_node_oid(mib_node)):])
                        index_str = '.' + '.'.join([str(i) for i in indices]) if indices else ''
                        
                        symbolic_oid = f"{module_name}::{obj_name}{index_str}"
                    except Exception:
                        symbolic_oid = oid.prettyPrint()
                
                # Format the value based on its type
                value_type = type(value).__name__.upper()
                formatted_value = format_snmp_output_value(value, value_type)
                
                print(f"{symbolic_oid} = {formatted_value}")
                
                # Append formatted output
                result.append(f"{symbolic_oid} = {formatted_value}")

    # End timing
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time:.2f} seconds")
    print(f"SNMP walk completed. Found {len(result)} OIDs.")
    return result

# Function to convert hex MAC to formatted string
def format_mac(hex_mac):
    # Remove spaces and format as XX:XX:XX:XX:XX:XX
    clean_mac = hex_mac.replace(" ", "")
    formatted_mac = ":".join([clean_mac[i:i+2] for i in range(0, len(clean_mac), 2)])
    return formatted_mac

# Function to convert received optical power from INTEGER32 to dBm
def convert_power_to_dbm(power_value):
    # Optical power is typically stored in units of 0.1 dBm or 0.01 dBm
    # The value -2268 suggests units of 0.01 dBm, hence division by 100.
    return float(power_value) / 100.0  # Divide by 100 for dBm value

# Function to parse SNMP output and extract ONU data
def parse_onu_data(data_str): # Renamed argument to avoid conflict with internal 'data' variables
    onu_data = {} # This dictionary will use string keys for ONU indices

    # Helper to initialize ONU entry if it doesn't exist and set IFINDEX
    def ensure_onu_entry(index_key_str):
        if index_key_str not in onu_data:
            onu_data[index_key_str] = {}
            # Populate IFINDEX using the string key, converted to an integer
            onu_data[index_key_str]['IFINDEX'] = int(index_key_str)

    # MAC Address
    mac_matches = re.findall(r'NSCRTV-FTTX-EPON-MIB::onuMacAddress\.(\d+) = Hex-STRING: ([0-9A-F ]+)', data_str)
    for index_s, mac in mac_matches:
        ensure_onu_entry(index_s)
        onu_data[index_s]['MAC'] = format_mac(mac)
        
    # Serial Number
    sn_matches = re.findall(r'NSCRTV-FTTX-EPON-MIB::onuSn\.(\d+) = Hex-STRING: ([0-9A-F ]+)', data_str)
    for index_s, sn in sn_matches:
        ensure_onu_entry(index_s)
        onu_data[index_s]['SLNO'] = format_mac(sn)
    
    # Operation Status - Made INTEGER32 optional in regex
    status_matches = re.findall(r'NSCRTV-FTTX-EPON-MIB::onuOperationStatus\.(\d+) = INTEGER(?:32)?: (\d+)', data_str)
    for index_s, status_val in status_matches:
        ensure_onu_entry(index_s)
        onu_data[index_s]['STATUS'] = int(status_val)
    
    # Admin Status - Made INTEGER32 optional in regex
    admin_matches = re.findall(r'NSCRTV-FTTX-EPON-MIB::onuAdminStatus\.(\d+) = INTEGER(?:32)?: (\d+)', data_str)
    for index_s, status_val in admin_matches:
        ensure_onu_entry(index_s)
        # Assuming '2' means disabled, and you want to map it to status '3'
        if str(status_val) == '2': 
            onu_data[index_s]['STATUS'] = 3 
    
    # Distance - Made INTEGER32 optional in regex
    distance_matches = re.findall(r'NSCRTV-FTTX-EPON-MIB::onuTestDistance\.(\d+) = INTEGER(?:32)?: (\d+)', data_str)
    for index_s, distance in distance_matches:
        ensure_onu_entry(index_s)
        onu_data[index_s]['DISTANCE'] = int(distance)
    
    # Time Since Last Register (for UP_SINCE calculation)
    # Sample output shows "Counter32: 5954", assuming value is in seconds.
    time_matches = re.findall(r'NSCRTV-FTTX-EPON-MIB::onuTimeSinceLastRegister\.(\d+) = Counter32: (\d+)', data_str)
    for index_s, seconds_str in time_matches:
        ensure_onu_entry(index_s)
        current_time = datetime.now()
        up_since = current_time - timedelta(seconds=int(seconds_str))
        onu_data[index_s]['UP_SINCE'] = up_since
    
    # Vendor ID
    vendor_matches = re.findall(r'NSCRTV-FTTX-EPON-MIB::onuVendorId\.(\d+) = Hex-STRING: ([0-9A-F ]+)', data_str)
    for index_s, vendor_hex in vendor_matches:
        ensure_onu_entry(index_s)
        # Convert hex to ASCII, filtering only printable characters
        vendor = ''.join([chr(int(h, 16)) for h in vendor_hex.split() if 32 <= int(h, 16) <= 126])
        onu_data[index_s]['ONU_VENDOR'] = vendor.strip()
    
    # Model ID - Made regex for string non-greedy and improved hex decoding
    model_matches = re.findall(r'NSCRTV-FTTX-EPON-MIB::onuModelId\.(\d+) = (?:STRING: "([^"]*)"|Hex-STRING: ([0-9A-F ]+))', data_str)
    for match in model_matches:
        index_s = match[0]
        ensure_onu_entry(index_s)
        
        model_str_val = match[1]  # Captured group for STRING
        model_hex_val = match[2]  # Captured group for Hex-STRING
        model = ""

        if model_str_val is not None: # Check if STRING part matched
            model = model_str_val.split('(')[0].strip() # Remove hex part if present, e.g. "ModelName (0123ABCD)"
        elif model_hex_val is not None: # Check if Hex-STRING part matched
            try:
                # Remove spaces before converting hex to bytes
                byte_data = bytes.fromhex(model_hex_val.replace(" ", ""))
                model = byte_data.decode('utf-8', errors='ignore').strip()
            except ValueError: 
                model = "" # Or log an error
        onu_data[index_s]['ONU_MODEL'] = model
    
    # Received Optical Power - Made INTEGER32 optional in regex
    power_matches = re.findall(r'NSCRTV-FTTX-EPON-MIB::onuReceivedOpticalPower\.(\d+)\.(\d+)\.(\d+) = INTEGER(?:32)?: (-?\d+)', data_str)
    for index_s, port1, port2, power_val_str in power_matches: # index_s is the string ONU index
        ensure_onu_entry(index_s) # Use the string index as the key
        
        # For onu_num calculation, int(index_s) is fine
        onu_num_val = int(index_s) & 0xFF 
        onu_data[index_s]['POWER'] = convert_power_to_dbm(power_val_str)
        onu_data[index_s]['IFINDEX2'] = f'epon0/{port1}/{port2}/{onu_num_val}'
    
    return onu_data

# Function to insert data into Oracle database
def insert_into_db(onu_data, ip, db_host, db_port, db_user, db_pass, db_sid):
    # Create DSN
    dsn_tns = cx_Oracle.makedsn(db_host, db_port, sid=db_sid)
    
    try:
        # Establish connection
        connection = cx_Oracle.connect(db_user, db_pass, dsn_tns)
        cursor = connection.cursor()
        
        print(f"Connected to Oracle Database.")
        
        # Get the switch ID from the SWITCHES table based on IP address
        try:
            cursor.execute("SELECT ID FROM SWITCHES WHERE IP = :ip", {"ip": ip})
            result = cursor.fetchone()
            sw_id = result[0] if result else None
            if sw_id:
                print(f"Retrieved switch ID {sw_id} from SWITCHES table for IP {ip}")
            else:
                print(f"Warning: No switch found with IP {ip} in SWITCHES table. SW_ID will be set to NULL.")
        except cx_Oracle.DatabaseError as e:
            error, = e.args
            print(f"Error retrieving switch ID from SWITCHES table: {error.message}")
            sw_id = None
        
        # Add SW_ID to each ONU record
        for index, data in onu_data.items():
            data['SW_ID'] = sw_id  # Add the retrieved SW_ID or None
        
        # Get the current timestamp for UDATE
        current_time = datetime.now()
        
        # filter to check if the ONU is online by checking POWER is not None and STATUS is 1
        # active_onu_data = {index: data for index, data in onu_data.items() if data.get('POWER') is not None and data.get('STATUS') == 1}
        # if not onu_data:
        #     print("No ONU records to insert. Exiting...")
        #     return True
        
        # Process each ONU record
        for index, data in onu_data.items():
            # Get next ID from the sequence SWITCH_SNMP_ONU_PORTS_sq
            cursor.execute("SELECT SWITCH_SNMP_ONU_PORTS_sq.nextval FROM DUAL")
            _id = cursor.fetchone()[0]
            # Set default values for missing fields
            data.setdefault('MAC', None)
            data.setdefault('POWER', None)
            data.setdefault('STATUS', None)
            data.setdefault('IFDESCR', None)
            data.setdefault('PORTNO', None)
            data.setdefault('IFINDEX', None)
            data.setdefault('ONU_PORT', None)
            data.setdefault('PON_PORT', None)
            data.setdefault('PARENT_ID', None)
            data.setdefault('SLNO', None)
            data.setdefault('DISTANCE', None)
            data.setdefault('UP_SINCE', None)
            data.setdefault('ONU_MODEL', None)
            data.setdefault('ONU_VENDOR', None)
            data.setdefault('IFINDEX2', None)
            
            # Insert the record
            cursor.execute("""
            INSERT INTO SWITCH_SNMP_ONU_PORTS 
            (ID, PORT_ID, MAC, POWER, STATUS, IFDESCR, PORTNO, SW_ID, IFINDEX, 
            UDATE, ONU_PORT, PON_PORT, PARENT_ID, SLNO, DISTANCE, UP_SINCE, ONU_MODEL, ONU_VENDOR, IFINDEX2)
            VALUES 
            (:id, :port_id, :mac, :power, :status, :ifdescr, :portno, :sw_id, :ifindex,
            :udate, :onu_port, :pon_port, :parent_id, :slno, :distance, :up_since, :onu_model, :onu_vendor, :ifindex2)
            """, {
                'id': _id,
                'port_id': None,
                'mac': data['MAC'],
                'power': data['POWER'],
                'status': data['STATUS'],
                'ifdescr': data['IFDESCR'],
                'portno': data['PORTNO'],
                'sw_id': sw_id,
                'ifindex': data['IFINDEX'],
                'udate': current_time,
                'onu_port': data['ONU_PORT'],
                'pon_port': data['PON_PORT'],
                'parent_id': data['PARENT_ID'],
                'slno': data['SLNO'],
                'distance': data['DISTANCE'],
                'up_since': data['UP_SINCE'],
                'onu_model': data['ONU_MODEL'],
                'onu_vendor': data['ONU_VENDOR'],
                'ifindex2': data['IFINDEX2']
            })
        
            # Commit the transaction
            connection.commit()
            print(f"Inserted record for ONU {index} with ID {_id} with {sw_id}")
            
        print(f"Successfully inserted {len(onu_data)} ONU records into the database.")
        
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        print(f"Database error: {error.message}")
        return False
    finally:
        # Close connection
        if 'connection' in locals():
            connection.close()
    
    return True

def insert_into_db_olt_customer_mac(onu_data, ip, db_host, db_port, db_user, db_pass, db_sid):
    # Create DSN
    dsn_tns = cx_Oracle.makedsn(db_host, db_port, sid=db_sid)
    
    try:
        # Establish connection
        connection = cx_Oracle.connect(db_user, db_pass, dsn_tns)
        cursor = connection.cursor()
        
        print(f"Connected to Oracle Database.")
        
        # Get the OLT ID from the SWITCHES table based on IP address
        try:
            cursor.execute("SELECT ID FROM SWITCHES WHERE IP = :ip", {"ip": ip})
            result = cursor.fetchone()
            olt_id = result[0] if result else None
            if olt_id:
                print(f"Retrieved OLT ID {olt_id} from SWITCHES table for IP {ip}")
            else:
                print(f"Warning: No OLT found with IP {ip} in SWITCHES table. SW_ID will be set to NULL.")
        except cx_Oracle.DatabaseError as e:
            error, = e.args
            print(f"Error retrieving OLT ID from SWITCHES table: {error.message}")
            olt_id = None
        
        # Add SW_ID to each ONU record
        for index, data in enumerate(onu_data):
            data['OLT_ID'] = olt_id  # Add the retrieved SW_ID or None
        
        # Get the current timestamp for UDATE
        current_time = datetime.now()
        
        # Process each ONU record
        for index, data in enumerate(onu_data):
            # Get next ID from the sequence OLT_CUSTOMER_MAC_sq
            cursor.execute("SELECT OLT_CUSTOMER_MAC_sq.nextval FROM DUAL")
            _id = cursor.fetchone()[0]
            # Set default values for missing fields
            data.setdefault('OLT_ID', None)
            data.setdefault('VLAN', None)
            data.setdefault('Port', None)
            data.setdefault('MAC', None)
            data.setdefault('udate', None)
            
            # Insert the record
            cursor.execute("""
            INSERT INTO OLT_CUSTOMER_MAC 
            (ID, OLT_ID, VLAN, PORT, MAC, UDATE)
            VALUES 
            (:id, :olt_id, :vlan, :port, :mac, :udate)
            """, {
                'id': _id,
                'olt_id': data['OLT_ID'],
                'vlan': data['VLAN'],
                'port': data['Port'],
                'mac': data['MAC'],
                'udate': current_time
            })
        
            # Commit the transaction
            connection.commit()
            print(f"Inserted record for ONU {index} with ID {_id} with {olt_id}")
            
        print(f"Successfully inserted {len(onu_data)} ONU records into the database.")
        
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        print(f"Database error: {error.message}")
        return False
    finally:
        # Close connection
        if 'connection' in locals():
            connection.close()
    
    return True