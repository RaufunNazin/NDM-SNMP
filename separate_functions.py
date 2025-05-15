from pysnmp.smi import view
from pysnmp.hlapi.v3arch.asyncio import *
import time
from utils import load_mibs, format_mac, convert_power_to_dbm
import asyncio
from convert import decode_epon_device_index

olt_information = {
    'mac': {
        'CDATA_EPON': '1.3.6.1.4.1.17409.2.3.4.1.1.7'
    },
    'oper_status': {
        'CDATA_EPON': '1.3.6.1.4.1.17409.2.3.4.1.1.8'
    },
    'admin_status': {
        'CDATA_EPON': '1.3.6.1.4.1.17409.2.3.4.1.1.9'
    },
    'distance': {
        'CDATA_EPON': '1.3.6.1.4.1.17409.2.3.4.1.1.15'
    },
    'up_since': {
        'CDATA_EPON': '1.3.6.1.4.1.17409.2.3.4.1.1.18'
    },
    'vendor': {
        'CDATA_EPON': '1.3.6.1.4.1.17409.2.3.4.1.1.25'
    },
    'model': {
        'CDATA_EPON': '1.3.6.1.4.1.17409.2.3.4.1.1.26'
    },
    'sn': {
        'CDATA_EPON': '1.3.6.1.4.1.17409.2.3.4.1.1.28'
    },
    'power': {
        'CDATA_EPON': '1.3.6.1.4.1.17409.2.3.4.2.1.4'
    } 
}

def format_cdata_values(value, value_type):
    """
    Format the value based on its type
    Args:
        value: The value to format.
        value_type (str): The type of the value (e.g., "OCTETSTRING", "INTEGER").
    Returns:
        str: The formatted value as a string.
    """
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
    
async def determine_olt_type(target_ip, community_string, port=161, version=0, retries=3, timeout=3, snmp_engine=None):
    """
    Determines OLT type (epon/gpon) by walking ifDescr.
    Args:
        target_ip (str): The IP address of the target device.
        community_string (str): The SNMP community string.
        port (int): SNMP port.
        version (int): SNMP version.
        retries (int): SNMP retries.
        timeout (int): SNMP timeout.
        snmp_engine (SnmpEngine, optional): An existing SnmpEngine instance. Defaults to None, creating a new one.
    Returns:
        str: "epon", "gpon", or "unknown".
    """
    if_descr_oid = '1.3.6.1.2.1.2.2.1.2'  # ifDescr
    determined_type = "unknown"

    engine = snmp_engine or SnmpEngine()
    
    try:
        async for errorIndication, errorStatus, errorIndex, varBinds in walk_cmd(
            engine,
            CommunityData(community_string, mpModel=version),
            await UdpTransportTarget.create((target_ip, port), timeout=timeout, retries=retries),
            ContextData(),
            ObjectType(ObjectIdentity(if_descr_oid)),
            lexicographicMode=False
        ):
            if errorIndication:
                print(f"OLT Type Determination - SNMP Error: {errorIndication}")
                break
            elif errorStatus:
                print(f"OLT Type Determination - SNMP Status Error: {errorStatus.prettyPrint()} at {errorIndex and varBinds[int(errorIndex) - 1][0] or '?'}")
                break
            else:
                for varBind in varBinds:
                    _oid, value = varBind
                    # Value is typically OctetString for ifDescr
                    descr = ""
                    if hasattr(value, 'prettyPrint'):
                        descr = value.prettyPrint().lower()
                    elif isinstance(value, bytes): # Fallback for raw bytes
                        try:
                            descr = value.decode('utf-8', errors='ignore').lower()
                        except:
                             pass # Ignore decoding errors for non-string bytes

                    if 'epon' in descr:
                        determined_type = "epon"
                        return determined_type  # Found, can exit early
                    elif 'gpon' in descr:
                        determined_type = "gpon"
                        return determined_type  # Found, can exit early
    except Exception as e:
        print(f"Exception during OLT type determination: {e}")
    
    return determined_type

async def get_olt_information(target_ip, community_string, port=161, version=0, retries = 3, timeout = 3, branch = 'mac', brand='CDATA_EPON'):
    """
    Perform an SNMP walk operation to retrieve OLT information.
    Args:
        target_ip (str): The IP address of the target device.
        community_string (str): The SNMP community string.
        port (int): The SNMP port (default is 161).
        version (int): SNMP version (0 for v1, 1 for v2c, 3 for v3).
        retries (int): Number of retries for SNMP requests.
        timeout (int): Timeout in seconds for SNMP requests.
        branch (str): The branch of OLT information to retrieve.
        brand (str): The brand of the device.
    Returns:
        list: A list of strings containing the OLT information.
    """
    result = []
    # Start timing
    start_time = time.time()
    
    # Load all MIBs
    mib_builder = load_mibs()
    mib_view = view.MibViewController(mib_builder)
    
    # Create the generator for the SNMP walk operation
    objects = walk_cmd(
        SnmpEngine(),
        CommunityData(community_string, mpModel=version),
        await UdpTransportTarget.create((target_ip, port), timeout=timeout, retries=retries),
        ContextData(),
        ObjectType(ObjectIdentity(olt_information[branch][brand])),
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
                
                if(brand == 'CDATA_EPON' or brand == 'CDATA_GPON'):
                    formatted_value = format_cdata_values(value, value_type)
                else:
                    formatted_value = f"{value_type}: {value.prettyPrint()}"
                
                # Append formatted output
                result.append(f"{symbolic_oid} = {formatted_value}")

    # End timing
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time:.2f} seconds")
    print(f"SNMP walk completed. Found {len(result)} OIDs.")
    return result

def process_cdata(snmp_output_lines, olt_type):
    """
    Processes SNMP output lines to extract and structure data.
    The function assumes indices in the OIDs are EPON device IDs
    decodable by decode_epon_device_index.

    Args:
        snmp_output_lines (list): A list of strings, where each string is an SNMP output line.
                                  Example format: "MIB-NAME::objectName.index... = ValueType: ValueString"
        olt_type (str): The type of OLT, either 'epon' or 'gpon'. Default is 'epon'.

    Returns:
        list: An array of objects (list of dictionaries).
              Example: [{ "onuMacAddress": { "frameid1": "mac_val1", ... } },
                        { "onuReceivedOpticalPower": { "frameid2": power_val2, ... } }]
    """
    # This dictionary will store data like:
    # {
    #   "onuMacAddress": {"0/2/1/20": "A2:4F:02:18:E5:80"},
    #   "onuReceivedOpticalPower": {"0/2/3/16": -12.80},
    #   "onuOperationStatus": {"0/2/1/20": 1}
    # }
    processed_data_map = {}

    for line in snmp_output_lines:
        try:
            # Split OID part from value part
            # Example: "NSCRTV-FTTX-EPON-MIB::onuMacAddress.38285331 = Hex-STRING: A2 4F 02 18 E5 80"
            parts = line.split(" = ", 1)
            if len(parts) != 2:
                print(f"Warning: Skipping malformed line (no ' = ' separator): {line}")
                continue
            
            oid_full_str, value_full_str = parts

            # Extract OID key (e.g., "onuMacAddress") and the primary device_id string
            # Example oid_full_str: "NSCRTV-FTTX-EPON-MIB::onuMacAddress.38285331"
            # Example for power: "NSCRTV-FTTX-EPON-MIB::onuReceivedOpticalPower.38285328.2.4"
            
            oid_components = oid_full_str.split('.')
            if not oid_components:
                print(f"Warning: Skipping line with invalid OID format (empty components after split by '.'): {line}")
                continue

            # The first component is the MIB object name, possibly with MIB prefix
            # e.g., "NSCRTV-FTTX-EPON-MIB::onuMacAddress"
            oid_key_full_name = oid_components[0] 
            
            oid_key = oid_key_full_name
            if "::" in oid_key_full_name: # Extract the object name part if MIB prefix exists
                oid_key = oid_key_full_name.split("::", 1)[1]

            # The component after the object name should be the numeric device ID
            if len(oid_components) < 2 or not oid_components[1].isdigit():
                print(f"Warning: Could not extract valid numeric device ID from OID '{oid_full_str}' in line: {line}")
                continue
            device_id_str = oid_components[1] # This is the ID for decode_epon_device_index

            # Extract value type indicator (e.g., "Hex-STRING") and raw value string
            # Example value_full_str: "Hex-STRING: A2 4F 02 18 E5 80" or "INTEGER: -1280"
            value_parts = value_full_str.split(": ", 1)
            if len(value_parts) != 2:
                print(f"Warning: Skipping line with invalid value format (no ': ' separator): {line}")
                continue
            
            value_type_indicator = value_parts[0] # e.g., "Hex-STRING", "INTEGER", "Counter32"
            raw_value_str = value_parts[1]        # e.g., "A2 4F 02 18 E5 80", "-1280", "12345"

            # Decode device ID to frame ID using decode_epon_device_index
            device_id_int = int(device_id_str) # Can raise ValueError
            decoded_indices = decode_epon_device_index(device_id_int)
            slot_id = decoded_indices["Slot ID"]
            pon_id = decoded_indices["PON ID"]
            onu_id = decoded_indices["ONU ID"]
            frame_id = f"{olt_type}0/{slot_id}/{pon_id}/{onu_id}"

            # Parse the value based on OID key and value type
            parsed_value = None
            if "onuReceivedOpticalPower" in oid_key: # Specific handling for optical power
                try:
                    # raw_value_str is the numeric part, e.g., "-1280"
                    parsed_value = convert_power_to_dbm(int(raw_value_str))
                except ValueError:
                    print(f"Warning: Could not parse power value '{raw_value_str}' as int for line: {line}")
                    parsed_value = raw_value_str # Fallback
            elif value_type_indicator == "Hex-STRING":
                # As per prompt, other Hex-STRINGs are formatted like MAC (e.g. ONU SN, MAC)
                parsed_value = format_mac(raw_value_str)
            elif value_type_indicator.startswith("INTEGER") or \
                 value_type_indicator.startswith("GAUGE") or \
                 value_type_indicator.startswith("COUNTER"):
                try:
                    # For simple numeric types (INTEGER, COUNTER, GAUGE), try to convert to int
                    parsed_value = int(raw_value_str)
                except ValueError:
                    parsed_value = raw_value_str # Fallback if not a simple int
            elif value_type_indicator == "STRING":
                # For STRING type, remove surrounding quotes if present (e.g. "some value" -> some value)
                parsed_value = raw_value_str.strip('"')
            else:
                # Default for other types (e.g., Timeticks, IpAddress which are already formatted as strings)
                parsed_value = raw_value_str
            
            # Store in the map
            if oid_key not in processed_data_map:
                processed_data_map[oid_key] = {}
            processed_data_map[oid_key][frame_id] = parsed_value

        except ValueError as ve: # Catch potential int conversion errors for device_id_str
            print(f"Warning: ValueError processing line '{line}': {ve}")
        except Exception as e: # Catch any other unexpected errors during line processing
            print(f"Warning: Generic error processing line '{line}': {e}")

    # Convert map to the required list of dictionaries format
    result_array = []
    for key, value_map in processed_data_map.items():
        result_array.append({key: value_map})
        
    return result_array

def process_snmp_data(snmp_output_lines, brand, olt_type):
    """
    Process SNMP data based on the brand.
    
    Args:
        snmp_output_lines (list): A list of strings, where each string is an SNMP output line.
        brand (str): The brand of the device (e.g., 'CDATA_EPON').
        olt_type (str): The type of OLT, either 'epon' or 'gpon'.
    
    Returns:
        list: A list of dictionaries with processed data.
    """
    if brand == 'CDATA_EPON' or brand == 'CDATA_GPON':
        return process_cdata(snmp_output_lines, olt_type)
    else:
        print(f"Unsupported brand: {brand}")
        return []

async def main():
    target_ip = '10.12.1.13'
    community_string = 'faridsnmp'
    port = 161
    version = 0
    retries = 3
    timeout = 3
    branch = 'mac'
    
    # Get OLT type
    olt_type = await determine_olt_type(target_ip, community_string, port, version, retries, timeout)
    
    brand = f'CDATA_{olt_type.upper()}'
    
    # Call the function to get OLT information
    result = await get_olt_information(target_ip, community_string, port, version, retries, timeout, branch, brand)
    
    # Process the SNMP data
    processed_data = process_snmp_data(result, brand, olt_type)
    
    # Print the result
    for item in processed_data:
        for key, value in item.items():
            print(f"{key}:")
            for frame_id, parsed_value in value.items():
                print(f"  {frame_id}: {parsed_value}")
        
if __name__ == "__main__":
    asyncio.run(main())