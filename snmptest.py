import asyncio
from pysnmp.hlapi.v3arch.asyncio import *
from datetime import datetime
import time
import os
from dotenv import load_dotenv
from pysnmp.smi import builder, view

load_dotenv()

# SNMP target settings
target_ip = os.getenv("TARGET_IP")
community_string = os.getenv("COMMUNITY_STRING")
oid_to_walk = os.getenv("OID_TO_WALK")
snmp_version = 0 if(os.getenv("SNMP_VERSION") == "1") else 1 # 0 for SNMPv1, 1 for SNMPv2c
snmp_timeout = int(os.getenv("SNMP_TIMEOUT", 3))  # Timeout in seconds
snmp_retries = int(os.getenv("SNMP_RETRIES", 3))  # Number of retries

 
if not target_ip or not community_string or not oid_to_walk:
    raise ValueError("Please set TARGET_IP, COMMUNITY_STRING, and OID_TO_WALK in the .env file.")
if not snmp_version in [0, 1]:
    raise ValueError("Please set SNMP_VERSION to 1 for SNMPv1 or 2 for SNMPv2c in the .env file.")

# Output file
output_filename = "snmp_output.txt"

def load_mibs():
    """Load MIBs from both compiled directory and source directory"""
    print("Loading MIBs...")
    mib_builder = builder.MibBuilder()
    
    # Add compiled MIBs directory first (higher priority)
    compiled_mib_dir = 'compiled_mibs'
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

# Perform SNMP Walk using async walk_cmd
async def snmp_walk(ip, community, oid):
    result = []
    # Start timing
    start_time = time.time()
    
    # Load all MIBs
    mib_dir = 'mibs'
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
                formatted_value = format_value(value, value_type)
                
                # Append formatted output
                result.append(f"{symbolic_oid} = {formatted_value}")

    # End timing
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time:.2f} seconds")
    print(f"SNMP walk completed. Found {len(result)} OIDs.")
    return result

def format_value(value, value_type):
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

# Run and display
async def main():
    print("Running SNMP walk...")
    print(f"Target IP: {target_ip}")
    print(f"Community String: {community_string}")
    print(f"OID to walk: {oid_to_walk}")
    output = await snmp_walk(target_ip, community_string, oid_to_walk)

    # Save to file
    with open(output_filename, "w") as file:
        file.write(f"# SNMP Walk Output for {target_ip}\n")
        file.write(f"# Time: {datetime.now()}\n\n")
        file.write("\n".join(output))
    
    print(f"Output saved to {output_filename}")

if __name__ == "__main__":
    asyncio.run(main())
