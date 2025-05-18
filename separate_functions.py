import asyncio
from enums import MAC, OPERATION_STATUS, ADMIN_STATUS, DISTANCE, UP_SINCE, VENDOR, MODEL, SERIAL_NO, POWER, CDATA, CDATA_EPON, CDATA_GPON
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
    branches = {
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
    
    supported_brands = {
        "CDATA": CDATA
    }

    parser = argparse.ArgumentParser(description="SNMP OLT Information Retriever")
    parser.add_argument("-i", required=True, help="Target OLT IP address")
    parser.add_argument("-c", required=True, help="SNMP community string")
    parser.add_argument("-p", type=int, default=161, help="SNMP port (default: 161)")
    parser.add_argument("-bc", required=True, choices=list(branches.keys()),
                        help="OID branch to query (default: mac)")
    parser.add_argument("-bd", required=True, choices=list(supported_brands.keys()),
                        help="Brand prefix, e.g., CDATA. _EPON or _GPON will be appended based on detected OLT type (default: CDATA)")
    parser.add_argument("-v", type=int, default=0, choices=[0, 1], help="SNMP version (0 for v1, 1 for v2c; default: 0)")
    parser.add_argument("-r", type=int, default=3, help="SNMP retries (default: 3)")
    parser.add_argument("-t", type=int, default=3, help="SNMP timeout in seconds (default: 3)")
    parser.add_argument("-idx", type=str, default=None,
                        help="Specific interface index string to query (e.g., 'gpon0/0/1/12'). "
                             "If provided, performs an SNMP GET for this specific index.")
    parser.add_argument("-s", type=str, default=None, help="Specify if the outputs should be stored or not and add the file name")
    parser.add_argument("-cr", type=int, default=None, help="ONU Card ID/ required to encode to onuDeviceIndex")

    args = parser.parse_args()

    target_ip = args.i
    community_string = args.c
    port = args.p
    selected_branch_name = args.bc
    brand_prefix = args.bd
    snmp_version = args.v
    snmp_retries = args.r
    snmp_timeout = args.t
    interface_index_str = args.idx
    store_output = args.s
    card_id = args.cr
    
    selected_branch_constant = branches.get(selected_branch_name)
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
        brand=dynamic_brand_str_key,
        onu_index_str=interface_index_str,
        card_id=card_id
    )
    
    # Process the SNMP data
    # The 'brand' argument for process_snmp_data is used to check if it's CDATA_EPON or CDATA_GPON
    processed_data = process_snmp_data(result, brand=dynamic_brand_str_key, olt_type=olt_type)
    
    if store_output:
        # Store the output in a file
        with open(store_output, 'w') as f:
            for item in processed_data:
                for key, value_map in item.items():
                    f.write(f"\n--- {key} ---\n")
                    if not value_map:
                        f.write("  No entries found.\n")
                    for frame_id, parsed_value in value_map.items():
                        f.write(f"  {frame_id}: {parsed_value}\n")
        print(f"Output stored in {store_output}")
    else:
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