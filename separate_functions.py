from pysnmp.smi import view
from pysnmp.hlapi.v3arch.asyncio import *
import time
from utils import load_mibs, format_mac, convert_power_to_dbm
import asyncio
from convert import decode_epon_device_index
import re

olt_information = {
    'mac': {
        'CDATA': '1.3.6.1.4.1.17409.2.3.4.1.1.7'
    },
    'oper_status': {
        'CDATA': '1.3.6.1.4.1.17409.2.3.4.1.1.8'
    },
    'admin_status': {
        'CDATA': '1.3.6.1.4.1.17409.2.3.4.1.1.9'
    },
    'distance': {
        'CDATA': '1.3.6.1.4.1.17409.2.3.4.1.1.15'
    },
    'up_since': {
        'CDATA': '1.3.6.1.4.1.17409.2.3.4.1.1.18'
    },
    'vendor': {
        'CDATA': '1.3.6.1.4.1.17409.2.3.4.1.1.25'
    },
    'model': {
        'CDATA': '1.3.6.1.4.1.17409.2.3.4.1.1.26'
    },
    'sn': {
        'CDATA': '1.3.6.1.4.1.17409.2.3.4.1.1.28'
    },
    'power': {
        'CDATA': '1.3.6.1.4.1.17409.2.3.4.2.1.4'
    } 
}

def format_cdata_values(value, value_type):
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

async def get_olt_information(target_ip, community_string, port=161, version=0, retries = 3, timeout = 3, branch = 'mac', brand='CDATA'):
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
                
                if(brand == 'CDATA'):
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

def process_snmp_data(snmp_output_lines):
    """
    Processes SNMP output lines to extract and structure data.

    Args:
        snmp_output_lines (list): A list of strings, where each string is an SNMP output line.

    Returns:
        list: An array of objects (list of dictionaries) containing parsed data.
              Example: [{ "macAddress": { "frameid1": "mac_val1", ... } },
                        { "ReceivedOpticalPower": { "frameid2": "power_val2", ... } }]
    """
    mac_address_data = {}
    optical_power_data = {}

    # Regex for NSCRTV-FTTX-EPON-MIB::onuMacAddress
    # Example: NSCRTV-FTTX-EPON-MIB::onuMacAddress.38285331 = Hex-STRING: A2 4F 02 18 E5 80
    mac_regex = re.compile(
        r"NSCRTV-FTTX-EPON-MIB::onuMacAddress\.(\d+) = Hex-STRING: ([\dA-Fa-f\s]+)"
    )

    # Regex for NSCRTV-FTTX-EPON-MIB::onuReceivedOpticalPower
    # Example: NSCRTV-FTTX-EPON-MIB::onuReceivedOpticalPower.38285328.2.4 = INTEGER32: -1280
    power_regex = re.compile(
        r"NSCRTV-FTTX-EPON-MIB::onuReceivedOpticalPower\.(\d+)(?:\.\d+)* = \w+: (-?\d+)"
    )

    for line in snmp_output_lines:
        mac_match = mac_regex.match(line)
        power_match = power_regex.match(line)

        device_id_str = None
        value_str = None
        data_dict_to_update = None
        value_parser = None
        is_mac = False

        if mac_match:
            device_id_str = mac_match.group(1)
            value_str = mac_match.group(2)
            data_dict_to_update = mac_address_data
            value_parser = format_mac
            is_mac = True
        elif power_match:
            device_id_str = power_match.group(1)
            value_str = power_match.group(2) # This is the numeric part as a string
            data_dict_to_update = optical_power_data
            # convert_power_to_dbm expects an int or float, regex captures string
            value_parser = lambda x: convert_power_to_dbm(int(x))


        if device_id_str and data_dict_to_update is not None and value_parser:
            try:
                device_id_int = int(device_id_str)
                decoded_indices = decode_epon_device_index(device_id_int)

                slot_id = decoded_indices["Slot ID"]
                pon_id = decoded_indices["PON ID"]
                onu_id = decoded_indices["ONU ID"]

                frame_id = f"0/{slot_id}/{pon_id}/{onu_id}"
                
                parsed_value = value_parser(value_str)
                data_dict_to_update[frame_id] = parsed_value

            except ValueError:
                print(f"Warning: Could not parse device ID '{device_id_str}' or value '{value_str}' for line: {line}")
            except Exception as e:
                print(f"Warning: Error processing line '{line}': {e}")

    result_array = []
    if mac_address_data:
        result_array.append({"macAddress": mac_address_data})
    if optical_power_data:
        result_array.append({"ReceivedOpticalPower": optical_power_data})

    return result_array

async def main():
    target_ip = '10.12.1.13'
    community_string = 'faridsnmp'
    port = 161
    version = 0
    retries = 3
    timeout = 3
    branch = 'mac'
    brand = 'CDATA'
    
    # Call the function to get OLT information
    result = await get_olt_information(target_ip, community_string, port, version, retries, timeout, branch, brand)
    # Process the SNMP data
    processed_data = process_snmp_data(result)
    
    # Print the result
    for item in processed_data:
        for key, value in item.items():
            print(f"{key}:")
            for frame_id, parsed_value in value.items():
                print(f"  {frame_id}: {parsed_value}")
        
if __name__ == "__main__":
    asyncio.run(main())