from pysnmp.smi import view
from pysnmp.hlapi.v3arch.asyncio import *
import time
from utils import load_mibs
import asyncio

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
    
    # Print the result
    for line in result:
        print(line)
        
if __name__ == "__main__":
    asyncio.run(main())