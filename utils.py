from pysnmp.smi import builder, view
import re
from datetime import datetime, timedelta
from pysnmp.hlapi.v3arch.asyncio import *
import time
import os
from enums import COMPILED_MIBS
import cx_Oracle

# Function to load MIBs
def load_mibs():
    """Load MIBs from both compiled directory and source directory"""
    print("Loading MIBs...")
    mib_builder = builder.MibBuilder()
    
    # Add compiled MIBs directory first (higher priority)
    compiled_mib_dir = COMPILED_MIBS
    if os.path.exists(compiled_mib_dir):
        mib_builder.add_mib_sources(builder.DirMibSource(compiled_mib_dir))
        print(f"Added compiled MIBs path: {compiled_mib_dir}")
    
    
    # Also add source MIBs directory as last resort
    source_mib_dir = 'mibs'
    mib_builder.add_mib_sources(builder.DirMibSource(source_mib_dir))
    print(f"Added source MIBs path: {source_mib_dir}")
    
    # Try to load important MIBs
    core_mibs = [
    'SNMPv2-MIB', 'SNMPv2-SMI', 'SNMPv2-TC', 'SNMPv2-CONF', 
    'RFC1213-MIB', 'IF-MIB', 'IP-MIB', 'MIKROTIK-MIB',
    'IANAifType-MIB', 'BRIDGE-MIB', 'HOST-RESOURCES-MIB', 
    'ENTITY-MIB', 'IEEE802dot11-MIB', 'IANA-ENTITY-MIB', 'RMON-MIB', 'CDATA-EPON-MIB', 'CDATA-GPON-MIB', 'CDATA-COMMON-SMI', 'NSCRTV-FTTX-EPON-MIB', 'NSCRTV-FTTX-GPON-MIB'
    ]
    
    for mib in core_mibs:
        try:
            mib_builder.load_modules(mib)
            print(f"Loaded MIB: {mib}")
        except Exception as e:
            print(f"Warning: Could not load MIB {mib}: {e}")
    
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
async def snmp_walk(ip, community, oid, snmp_version=0, snmp_timeout=3, snmp_retries=3):
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
        await UdpTransportTarget.create((ip, 161), timeout=snmp_timeout, retries=snmp_retries),
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
    # The negative values indicate it's in 0.1 dBm
    return float(power_value) / 100.0  # Divide by 100 for dBm value

# Function to parse SNMP output and extract ONU data
def parse_onu_data(data):
    onu_data = {}
    
    # Extract data using regex patterns
    # MAC Address
    mac_matches = re.findall(r'NSCRTV-FTTX-EPON-MIB::onuMacAddress\.(\d+) = Hex-STRING: ([0-9A-F ]+)', data)
    for index, mac in mac_matches:
        if index not in onu_data:
            onu_data[index] = {}
        onu_data[index]['MAC'] = format_mac(mac)
        onu_data[index]['IFINDEX'] = int(index)
        
    # Serial Number
    sn_matches = re.findall(r'NSCRTV-FTTX-EPON-MIB::onuSn\.(\d+) = Hex-STRING: ([0-9A-F ]+)', data)
    for index, sn in sn_matches:
        if index not in onu_data:
            onu_data[index] = {}
        onu_data[index]['SLNO'] = format_mac(sn)
    
    # Operation Status
    status_matches = re.findall(r'NSCRTV-FTTX-EPON-MIB::onuOperationStatus\.(\d+) = INTEGER32: (\d+)', data)
    for index, status in status_matches:
        if index not in onu_data:
            onu_data[index] = {}
        onu_data[index]['STATUS'] = int(status)
    
    # Admin Status
    admin_matches = re.findall(r'NSCRTV-FTTX-EPON-MIB::onuAdminStatus\.(\d+) = INTEGER32: (\d+)', data)
    for index, status in admin_matches:
        if index not in onu_data:
            onu_data[index] = {}
        if str(status) == '2':
            onu_data[index]['STATUS'] = 3
    
    # Distance
    distance_matches = re.findall(r'NSCRTV-FTTX-EPON-MIB::onuTestDistance\.(\d+) = INTEGER32: (\d+)', data)
    for index, distance in distance_matches:
        if index not in onu_data:
            onu_data[index] = {}
        onu_data[index]['DISTANCE'] = int(distance)
    
    # Time Since Last Register (for UP_SINCE calculation)
    time_matches = re.findall(r'NSCRTV-FTTX-EPON-MIB::onuTimeSinceLastRegister\.(\d+) = Counter32: (\d+)', data)
    for index, seconds in time_matches:
        if index not in onu_data:
            onu_data[index] = {}
        # Calculate UP_SINCE date based on current time minus the seconds
        current_time = datetime.now()
        up_since = current_time - timedelta(seconds=int(seconds))
        onu_data[index]['UP_SINCE'] = up_since
    
    # Vendor ID
    vendor_matches = re.findall(r'NSCRTV-FTTX-EPON-MIB::onuVendorId\.(\d+) = Hex-STRING: ([0-9A-F ]+)', data)
    for index, vendor_hex in vendor_matches:
        if index not in onu_data:
            onu_data[index] = {}
        # Convert hex to ASCII, filtering only printable characters
        vendor = ''.join([chr(int(h, 16)) for h in vendor_hex.split() if int(h, 16) >= 32 and int(h, 16) <= 126])
        onu_data[index]['ONU_VENDOR'] = vendor.strip()
    
    # Model ID
    model_matches = re.findall(r'NSCRTV-FTTX-EPON-MIB::onuModelId\.(\d+) = (?:STRING: "([^"]+)"|Hex-STRING: ([0-9A-F ]+))', data)
    for match in model_matches:
        index = match[0]
        if index not in onu_data:
            onu_data[index] = {}
        
        # If it's a string value
        if match[1]:
            model = match[1].split('(')[0]  # Remove the hex part if present
            onu_data[index]['ONU_MODEL'] = model.strip()
        # If it's a hex value
        elif match[2]:
            hex_value = match[2]
            try:
                # Convert hex string to bytes
                byte_data = bytes.fromhex(hex_value)
                model = byte_data.decode('utf-8', errors='ignore')
            except Exception as e:
                model = ''
            onu_data[index]['ONU_MODEL'] = model.strip()
    
    # Received Optical Power
    power_matches = re.findall(r'NSCRTV-FTTX-EPON-MIB::onuReceivedOpticalPower\.(\d+)\.(\d+)\.(\d+) = INTEGER32: (-?\d+)', data)
    for index_str, port1, port2, power in power_matches:
        index = int(index_str)
        onu_num = index & 0xFF
        if index not in onu_data:
            onu_data[index] = {}
        # Store both the raw value and converted dBm value
        onu_data[index]['POWER'] = convert_power_to_dbm(power)
        onu_data[index]['IFINDEX2'] = f'epon0/{port1}/{port2}/{onu_num}'
    
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
        for index, data in onu_data.items():
            data['OLT_ID'] = olt_id  # Add the retrieved SW_ID or None
        
        # Get the current timestamp for UDATE
        current_time = datetime.now()
        
        # Process each ONU record
        for index, data in onu_data.items():
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