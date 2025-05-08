import re
import cx_Oracle
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
import argparse  # Add import for command line argument parsing

# TODO: remove hardcoded ip address and PORT_ID = None, PON_PORT = None, PARENT_ID = None, ONU_PORT = None

# Load environment variables
load_dotenv()

# Oracle DB connection settings
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")
db_sid = os.getenv("DB_SID")
target_ip = os.getenv("TARGET_IP")

# Initialize Oracle client
cx_Oracle.init_oracle_client(lib_dir="/snap/instantclient_23_8")

# SNMP output file
input_file = "snmp_output.txt"

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
def parse_onu_data(file_path):
    onu_data = {}
    
    # Read the file
    with open(file_path, 'r') as file:
        content = file.read()
    
    # Extract data using regex patterns
    # MAC Address
    mac_matches = re.findall(r'NSCRTV-FTTX-EPON-MIB::onuMacAddress\.(\d+) = Hex-STRING: ([0-9A-F ]+)', content)
    for index, mac in mac_matches:
        if index not in onu_data:
            onu_data[index] = {}
        onu_data[index]['MAC'] = format_mac(mac)
        onu_data[index]['IFINDEX'] = int(index)
        
    # Serial Number
    sn_matches = re.findall(r'NSCRTV-FTTX-EPON-MIB::onuSn\.(\d+) = Hex-STRING: ([0-9A-F ]+)', content)
    for index, sn in sn_matches:
        if index not in onu_data:
            onu_data[index] = {}
        onu_data[index]['SLNO'] = format_mac(sn)
    
    # Operation Status
    status_matches = re.findall(r'NSCRTV-FTTX-EPON-MIB::onuOperationStatus\.(\d+) = INTEGER32: (\d+)', content)
    for index, status in status_matches:
        if index not in onu_data:
            onu_data[index] = {}
        if str(status) == '1':
            onu_data[index]['STATUS'] = 1
        elif str(status) == '0':
            onu_data[index]['STATUS'] = 2
    
    # Admin Status
    admin_matches = re.findall(r'NSCRTV-FTTX-EPON-MIB::onuAdminStatus\.(\d+) = INTEGER32: (\d+)', content)
    for index, status in admin_matches:
        if index not in onu_data:
            onu_data[index] = {}
        if str(status) == '0':
            onu_data[index]['STATUS'] = 3
    
    # Distance
    distance_matches = re.findall(r'NSCRTV-FTTX-EPON-MIB::onuTestDistance\.(\d+) = INTEGER32: (\d+)', content)
    for index, distance in distance_matches:
        if index not in onu_data:
            onu_data[index] = {}
        onu_data[index]['DISTANCE'] = int(distance)
    
    # Time Since Last Register (for UP_SINCE calculation)
    time_matches = re.findall(r'NSCRTV-FTTX-EPON-MIB::onuTimeSinceLastRegister\.(\d+) = Counter32: (\d+)', content)
    for index, seconds in time_matches:
        if index not in onu_data:
            onu_data[index] = {}
        # Calculate UP_SINCE date based on current time minus the seconds
        current_time = datetime.now()
        up_since = current_time - timedelta(seconds=int(seconds))
        onu_data[index]['UP_SINCE'] = up_since
    
    # Vendor ID
    vendor_matches = re.findall(r'NSCRTV-FTTX-EPON-MIB::onuVendorId\.(\d+) = Hex-STRING: ([0-9A-F ]+)', content)
    for index, vendor_hex in vendor_matches:
        if index not in onu_data:
            onu_data[index] = {}
        # Convert hex to ASCII, filtering only printable characters
        vendor = ''.join([chr(int(h, 16)) for h in vendor_hex.split() if int(h, 16) >= 32 and int(h, 16) <= 126])
        onu_data[index]['ONU_VENDOR'] = vendor.strip()
    
    # Model ID
    model_matches = re.findall(r'NSCRTV-FTTX-EPON-MIB::onuModelId\.(\d+) = (?:STRING: "([^"]+)"|Hex-STRING: ([0-9A-F ]+))', content)
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
    power_matches = re.findall(r'NSCRTV-FTTX-EPON-MIB::onuReceivedOpticalPower\.(\d+)\.(\d+)\.(\d+) = INTEGER32: (-?\d+)', content)
    for index, port1, port2, power in power_matches:
        if index not in onu_data:
            onu_data[index] = {}
        # Store both the raw value and converted dBm value
        onu_data[index]['POWER'] = convert_power_to_dbm(power)
    
    return onu_data

# Function to insert data into Oracle database
def insert_into_db(onu_data):
    # Create DSN
    dsn_tns = cx_Oracle.makedsn(db_host, db_port, sid=db_sid)
    
    try:
        # Establish connection
        connection = cx_Oracle.connect(db_user, db_pass, dsn_tns)
        cursor = connection.cursor()
        
        print(f"Connected to Oracle Database. Will insert {len(onu_data)} records...")
        
        # Get the switch ID from the SWITCHES table based on IP address
        try:
            cursor.execute("SELECT ID FROM SWITCHES WHERE IP = :ip", {"ip": target_ip})
            result = cursor.fetchone()
            sw_id = result[0] if result else None
            if sw_id:
                print(f"Retrieved switch ID {sw_id} from SWITCHES table for IP {target_ip}")
            else:
                print(f"Warning: No switch found with IP {target_ip} in SWITCHES table. SW_ID will be set to NULL.")
        except cx_Oracle.DatabaseError as e:
            error, = e.args
            print(f"Error retrieving switch ID from SWITCHES table: {error.message}")
            sw_id = None
        
        # Add SW_ID to each ONU record
        for index, data in onu_data.items():
            data['SW_ID'] = sw_id  # Add the retrieved SW_ID or None
        
        # Get the current timestamp for UDATE
        current_time = datetime.now()
        
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
            
            # Insert the record
            cursor.execute("""
            INSERT INTO SWITCH_SNMP_ONU_PORTS 
            (ID, PORT_ID, MAC, POWER, STATUS, IFDESCR, PORTNO, SW_ID, IFINDEX, 
            UDATE, ONU_PORT, PON_PORT, PARENT_ID, SLNO, DISTANCE, UP_SINCE, ONU_MODEL, ONU_VENDOR)
            VALUES 
            (:id, :port_id, :mac, :power, :status, :ifdescr, :portno, :sw_id, :ifindex,
            :udate, :onu_port, :pon_port, :parent_id, :slno, :distance, :up_since, :onu_model, :onu_vendor)
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
                'onu_vendor': data['ONU_VENDOR']
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

# Main function
def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Process ONU data from SNMP output and insert into database')
    parser.add_argument('-i', '--input-file', default='snmp_output.txt', help='Input SNMP output file (default: snmp_output.txt)')
    parser.add_argument('-d', '--dry-run', action='store_true', help='Parse data but do not insert into database')
    args = parser.parse_args()
    
    # Update input file based on argument
    global input_file
    input_file = args.input_file
    
    print(f"Starting ONU data processing from {input_file}...")
    
    # Parse the ONU data from SNMP output
    onu_data = parse_onu_data(input_file)
    
    # Print summary of parsed data
    print(f"Parsed {len(onu_data)} ONU devices from SNMP output.")
    
    # Example of first record
    if onu_data:
        first_key = list(onu_data.keys())[0]
        print(f"Sample record (ONU {first_key}):")
        for field, value in onu_data[first_key].items():
            print(f"  {field}: {value}")
    
    # Insert into database unless dry run is specified
    if not args.dry_run:
        insert_into_db(onu_data)
    else:
        print("Dry run mode: Data not inserted into database")

if __name__ == "__main__":
    main()