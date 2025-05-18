import asyncio
from enums import MAC, OPERATION_STATUS, ADMIN_STATUS, DISTANCE, UP_SINCE, VENDOR, MODEL, SERIAL_NO, POWER, CDATA_EPON, CDATA_GPON
import argparse
from helper import get_olt_type, get_olt_information
from process_data import process_cdata

def process_snmp_data(snmp_output_lines, brand, olt_type):
    """
    Process SNMP data based on the brand.
    
    Args:
        snmp_output_lines (list): A list of strings, where each string is an SNMP output line.
        brand (str): The brand of the device (e.g., CDATA_EPON).
        olt_type (str): The type of OLT, either 'epon' or 'gpon'.
    
    Returns:
        list: A list of dictionaries with processed data.
    """
    if brand == CDATA_EPON or brand == CDATA_GPON:
        return process_cdata(snmp_output_lines, olt_type)
    else:
        print(f"Unsupported brand: {brand}")
        return []

async def main():
    # Define a mapping from string names (used in CLI) to the actual enum constants for branches
    branch_name_to_constant_map = {
        "MAC": MAC,
        "OPERATION_STATUS": OPERATION_STATUS,
        "ADMIN_STATUS": ADMIN_STATUS,
        "DISTANCE": DISTANCE,
        "UP_SINCE": UP_SINCE,
        "VENDOR": VENDOR,
        "MODEL": MODEL,
        "SERIAL_NO": SERIAL_NO,
        "POWER": POWER,
    }

    parser = argparse.ArgumentParser(description="SNMP OLT Information Retriever")
    parser.add_argument("--ip", required=True, help="Target OLT IP address")
    parser.add_argument("--community", required=True, help="SNMP community string")
    parser.add_argument("--port", type=int, default=161, help="SNMP port (default: 161)")
    parser.add_argument("--branch", default=MAC, choices=list(branch_name_to_constant_map.keys()),
                        help="OID branch to query (default: mac)")
    parser.add_argument("--brand-prefix", default="CDATA",
                        help="Brand prefix, e.g., CDATA. _EPON or _GPON will be appended based on detected OLT type (default: CDATA)")
    parser.add_argument("--version", type=int, default=0, choices=[0, 1], help="SNMP version (0 for v1, 1 for v2c; default: 0)")
    parser.add_argument("--retries", type=int, default=3, help="SNMP retries (default: 3)")
    parser.add_argument("--timeout", type=int, default=3, help="SNMP timeout in seconds (default: 3)")

    args = parser.parse_args()

    target_ip = args.ip
    community_string = args.community
    port = args.port
    selected_branch_name = args.branch
    brand_prefix = args.brand_prefix
    snmp_version = args.version
    snmp_retries = args.retries
    snmp_timeout = args.timeout
    
    selected_branch_constant = branch_name_to_constant_map.get(selected_branch_name)
    if selected_branch_constant is None:
        print(f"Error: Invalid branch name '{selected_branch_name}'.")
        return

    # Get OLT type
    print(f"Determining OLT type for {target_ip}...")
    olt_type = await get_olt_type(
        target_ip=target_ip,
        community_string=community_string,
        port=port,
        brand=brand_prefix,
        version=snmp_version,
        retries=snmp_retries,
        timeout=snmp_timeout
    )
    print(f"Determined OLT Type: {olt_type}")

    if olt_type == "unknown":
        print(f"Error: Could not determine OLT type for {target_ip}. Aborting.")
        return

    # Construct the dynamic brand string key (e.g., "CDATA_EPON")
    dynamic_brand_str_key = f"{brand_prefix.upper()}_{olt_type.upper()}"

    print(f"Querying branch '{selected_branch_name}' for brand '{dynamic_brand_str_key}'")

    # Call the function to get OLT information
    result = await get_olt_information(
        target_ip=target_ip,
        community_string=community_string,
        port=port,
        version=snmp_version,
        retries=snmp_retries,
        timeout=snmp_timeout,
        branch=selected_branch_constant,
        brand=dynamic_brand_str_key
    )
    
    # Process the SNMP data
    # The 'brand' argument for process_snmp_data is used to check if it's CDATA_EPON or CDATA_GPON
    processed_data = process_snmp_data(result, brand=dynamic_brand_str_key, olt_type=olt_type)
    
    # Print the result
    if not processed_data:
        print("No data processed.")
    for item in processed_data:
        for key, value_map in item.items():
            print(f"\n--- {key} ---")
            if not value_map:
                print("  No entries found.")
            for frame_id, parsed_value in value_map.items():
                print(f"  {frame_id}: {parsed_value}")
        
if __name__ == "__main__":
    asyncio.run(main())