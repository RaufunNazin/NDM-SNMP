from utils import format_mac, convert_power_to_dbm
from index_decoder import decode_cdata_epon, decode_cdata_gpon
from enums import HEX_STRING, GAUGE, INTEGER, STRING, COUNTER, NULL, SLOT_ID, CARD_ID, PON_ID, ONU_ID, EPON_LOWER, GPON_LOWER
from datetime import datetime, timedelta

def process_cdata(snmp_output_lines, olt_type):
    """
    Processes SNMP output lines to extract and structure data.

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
                print(oid_components, oid_components[1])
                continue
            device_id_str = oid_components[1] # IndexID

            # Extract value type indicator (e.g., "Hex-STRING") and raw value string
            # Example value_full_str: "Hex-STRING: A2 4F 02 18 E5 80" or "INTEGER: -1280"
            if ": " in value_full_str:
                value_parts = value_full_str.split(": ", 1)
                if len(value_parts) != 2:
                    print(f"Warning: Skipping line with invalid value format (no ': ' separator): {line}")
                    continue
                
                value_type_indicator = value_parts[0] # e.g., "Hex-STRING", INTEGER, "Counter32"
                raw_value_str = value_parts[1]        # e.g., "A2 4F 02 18 E5 80", "-1280", "12345"
            elif value_full_str == "":
                value_type_indicator = NULL
                raw_value_str = ""
            else:
                raw_value_str = value_full_str

            # Decode device ID to Logical ID using decode function
            device_id_int = int(device_id_str) # Can raise ValueError
            if olt_type == EPON_LOWER:
                decoded_indices = decode_cdata_epon(device_id_int)
            elif olt_type == GPON_LOWER:
                decoded_indices = decode_cdata_gpon(device_id_int)
            frame_id = 0
            slot_id = decoded_indices[SLOT_ID]
            card_id = decoded_indices[CARD_ID]
            pon_id = decoded_indices[PON_ID]
            onu_id = decoded_indices[ONU_ID]
            frame_id = f"{olt_type}{frame_id}/{slot_id}/{pon_id}/{onu_id}->{device_id_str}:{card_id}"

            # Parse the value based on OID key and value type
            parsed_value = None
            if "onuReceivedOpticalPower" in oid_key: # Specific handling for optical power
                try:
                    # raw_value_str is the numeric part, e.g., "-1280"
                    parsed_value = convert_power_to_dbm(int(raw_value_str))
                except ValueError:
                    print(f"Warning: Could not parse power value '{raw_value_str}' as int for line: {line}")
                    parsed_value = raw_value_str # Fallback
            elif "onuTimeSinceLastRegister" in oid_key: #Specific handling for time since last register
                try:
                    # raw_value_str is the numeric part, e.g., "12345"
                    current_time = datetime.now()
                    parsed_value = current_time - timedelta(seconds=int(raw_value_str))
                except ValueError:
                    print(f"Warning: Could not parse time value '{raw_value_str}' as int for line: {line}")
                    parsed_value = raw_value_str
            elif value_type_indicator == HEX_STRING:
                # As per prompt, other Hex-STRINGs are formatted like MAC (e.g. ONU SN, MAC)
                parsed_value = format_mac(raw_value_str)
            elif value_type_indicator.startswith(INTEGER) or \
                 value_type_indicator.startswith(GAUGE) or \
                 value_type_indicator.startswith(COUNTER):
                try:
                    # For simple numeric types (INTEGER, COUNTER, GAUGE), try to convert to int
                    parsed_value = int(raw_value_str)
                except ValueError:
                    parsed_value = raw_value_str # Fallback if not a simple int
            elif value_type_indicator == STRING:
                # For STRING type, remove surrounding quotes if present (e.g. "some value" -> some value)
                parsed_value = raw_value_str.strip('"')
            elif value_type_indicator == NULL:
                parsed_value = None
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