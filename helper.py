from pysnmp.smi import view
from pysnmp.hlapi.v3arch.asyncio import *
import time
from utils import load_mibs
from enums import OCTETSTRING, HEX_STRING, OID, OID_SHORT, GAUGE32, INTEGER, STRING, COUNTER32, COUNTER64, TIMETICKS, IPADDRESS, NULL, CDATA, EPON_LOWER, GPON_LOWER, PON_LOWER
from oid_dict import oid_dictionary, IFDESCR
from index_encoder import encode_index_from_string
from snmp_session import get_snmp_session

def format_raw_values(value, value_type):
    """
    Format the value based on its type
    Args:
        value: The value to format.
        value_type (str): The type of the value (e.g., OCTETSTRING, INTEGER).
    Returns:
        str: The formatted value as a string.
    """
    if value_type == OCTETSTRING:
        # Check if the value is a printable string
        decoded_value = value.prettyPrint()
        if not decoded_value:  
            return '""'
        if not decoded_value.startswith("0x") and all(32 <= ord(char) <= 126 for char in decoded_value):
            return f'{STRING}: "{decoded_value}"'
        else:
            hex_value = " ".join([f"{byte:02X}" for byte in value.asNumbers()])
            return f'{HEX_STRING}: {hex_value}'
    elif value_type == OID:
        return f"{OID_SHORT}: {value.prettyPrint()}"
    elif value_type == GAUGE32:
        return f"{GAUGE32}: {value}"
    elif value_type == COUNTER32:
        return f"{COUNTER32}: {value}"
    elif value_type == COUNTER64:
        return f"{Counter64}: {value}"
    elif value_type == TIMETICKS:
        raw_ticks = int(value)
        days = raw_ticks // (24 * 60 * 60 * 100)
        hours = (raw_ticks // (60 * 60 * 100)) % 24
        minutes = (raw_ticks // (60 * 100)) % 60
        seconds = (raw_ticks // 100) % 60
        milliseconds = raw_ticks % 100
        human_readable = f"{days} days, {hours}:{minutes:02}:{seconds:02}.{milliseconds:02}"
        return f"{TIMETICKS}: ({raw_ticks}) {human_readable}"
    elif value_type == IPADDRESS:
        return f"{IPADDRESS}: {value.prettyPrint()}"
    elif value_type == INTEGER:
        return f"{INTEGER}: {value}"
    elif value_type == NULL:
        return '""'
    else:
        return f"{value_type}: {value.prettyPrint()}"
    
async def get_olt_type(target_ip, community_string, port, brand, version, retries, timeout):
    """
    Determines OLT type (epon/gpon) by walking ifDescr.
    Args:
        target_ip (str): The IP address of the target device.
        community_string (str): The SNMP community string.
        port (int): SNMP port.
        brand (str): The brand of the device.
        version (int): SNMP version.
        retries (int): SNMP retries.
        timeout (int): SNMP timeout.
    Returns:
        str: "epon", "gpon", or "unknown".
    """
    if_descr_oid = IFDESCR  # ifDescr
    determined_type = "unknown"

    engine = SnmpEngine()
    
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
                         
                    if brand == CDATA:
                        if EPON_LOWER in descr:
                            determined_type = EPON_LOWER
                            return determined_type  # Found, can exit early
                        elif GPON_LOWER in descr or PON_LOWER in descr:
                            determined_type = GPON_LOWER
                            return determined_type  # Found, can exit early
    except Exception as e:
        print(f"Exception during OLT type determination: {e}")
    
    return determined_type

def resolve_oid(oid, mib_view):
    try:
        oid_obj = ObjectIdentity(oid)
        oid_obj.resolve_with_mib(mib_view)
        return oid_obj.prettyPrint()
    except Exception:
        try:
            mib_node = mib_view.get_node_name(oid)
            module_name = mib_node[0]
            obj_name = mib_node[1]
            indices = list(oid[len(mib_view.get_node_oid(mib_node)):])
            index_str = '.' + '.'.join(map(str, indices)) if indices else ''
            return f"{module_name}::{obj_name}{index_str}"
        except Exception:
            return oid.prettyPrint()


async def get_olt_information(target_ip, community_string, port, version, retries, timeout, branch, brand, onu_index_str, card_id, all_oid):
    """
    Perform an SNMP walk or get operation to retrieve OLT information.
    Returns all resolved OIDs and values as strings.
    """
    result = []
    start_time = time.time()

    # Load MIBs once
    mib_builder = load_mibs()
    mib_view = view.MibViewController(mib_builder)

    # SNMP Session
    snmp_engine, community, transport, context = await get_snmp_session(
        target_ip, port, community_string, version, timeout, retries
    )

    action_description = ""  # For logging purposes

    if onu_index_str:
        index = encode_index_from_string(onu_index_str, brand, card_id)
        
        if all_oid:
            action_description = f"bulk GET for all branches (index: {onu_index_str}, brand: {brand})"
            print(f"Starting {action_description}")
            
            object_types_to_fetch = []
            for current_branch_key, brand_map in oid_dictionary.items():
                if brand in brand_map:
                    base_oid_for_branch = brand_map[brand]
                    oid_to_query_for_branch = f'{base_oid_for_branch}.{index}'
                    object_types_to_fetch.append(ObjectType(ObjectIdentity(oid_to_query_for_branch)))
                else:
                    msg = f"Info: OID for branch '{current_branch_key}' with brand '{brand}' not found in dictionary. Skipping for index {onu_index_str}."
                    result.append(msg)
            
            if not object_types_to_fetch:
                if not any(item.startswith("Info:") for item in result): # Add error only if no info messages about skipping were added
                     result.append(f"Error: No OIDs found to query for brand '{brand}' and index '{onu_index_str}' with all_oid=True.")
                # No SNMP call needed if nothing to fetch
            else:
                # Perform a single SNMP GET with all collected ObjectTypes
                errorIndication, errorStatus, errorIndex, varBinds = await get_cmd(
                    snmp_engine,
                    community,
                    transport,
                    context,
                    *object_types_to_fetch # Unpack the list
                )

                if errorIndication:
                    result.append(f"Error during bulk SNMP GET: {errorIndication}")
                elif errorStatus:
                    failed_oid_str = '?'
                    if errorIndex is not None and 0 < int(errorIndex) <= len(object_types_to_fetch):
                        # errorIndex is 1-based for the list of OIDs passed to get_cmd
                        failed_oid_object = object_types_to_fetch[int(errorIndex) - 1]
                        failed_oid_str = str(failed_oid_object[0]) # Get the OID string from ObjectType
                    
                    result.append(f"SNMP Error during bulk GET: {errorStatus.prettyPrint()} (at OID like {failed_oid_str}, errorIndex: {errorIndex})")
                    # Process any varBinds that were successfully retrieved before the error
                    for oid_val, value_val in varBinds:
                        symbolic_oid = resolve_oid(oid_val, mib_view)
                        formatted_value = format_raw_values(value_val, type(value_val).__name__.upper())
                        result.append(f"{symbolic_oid} = {formatted_value}")
                else: # Success for all OIDs in the bulk GET
                    for oid_val, value_val in varBinds:
                        symbolic_oid = resolve_oid(oid_val, mib_view)
                        formatted_value = format_raw_values(value_val, type(value_val).__name__.upper())
                        result.append(f"{symbolic_oid} = {formatted_value}")
        
        else: # Single OID GET (onu_index_str is true, all_oid is false)
            action_description = f"GET for branch '{branch}' (index: {onu_index_str}, brand: {brand})"
            if branch not in oid_dictionary or brand not in oid_dictionary[branch]:
                error_msg = f"Error: OID for specified branch '{branch}' and brand '{brand}' not found in dictionary."
                print(f"{action_description} - {error_msg}")
                result.append(error_msg)
            else:
                oid_to_query = f'{oid_dictionary[branch][brand]}.{index}'
                print(f"Starting {action_description}, OID: {oid_to_query}")
                
                # Single SNMP get
                errorIndication, errorStatus, errorIndex, varBinds = await get_cmd(
                    snmp_engine,
                    community,
                    transport,
                    context,
                    ObjectType(ObjectIdentity(oid_to_query))
                )

                if errorIndication:
                    return [f"Error: {errorIndication}"] # Original behavior: return immediately
                elif errorStatus:
                    return [f"SNMP Error: {errorStatus.prettyPrint()} at {errorIndex and varBinds[int(errorIndex) - 1][0] or '?'}"] # Original behavior

                for oid, value in varBinds:
                    symbolic_oid = resolve_oid(oid, mib_view)
                    formatted_value = format_raw_values(value, type(value).__name__.upper())
                    result.append(f"{symbolic_oid} = {formatted_value}")
    
    else: # SNMP WALK (onu_index_str is False)
        if all_oid:
            # The prompt was specific to "for that index", so all_oid is not applied to walks here.
            # You could extend this to walk all base OIDs if onu_index_str is false and all_oid is true.
            print(f"Warning: 'all_oid=True' is currently ignored for SNMP WALK operations (when no ONU index is provided). Performing standard walk for branch '{branch}'.")

        action_description = f"WALK for branch '{branch}' (brand: {brand})"
        if branch not in oid_dictionary or brand not in oid_dictionary[branch]:
            error_msg = f"Error: OID for branch '{branch}' and brand '{brand}' not found in dictionary for walk."
            print(f"{action_description} - {error_msg}")
            result.append(error_msg)
        else:
            oid_to_walk = oid_dictionary[branch][brand]
            print(f"Starting {action_description}, Base OID: {oid_to_walk}")
            
            # SNMP walk
            objects_to_walk = walk_cmd(
                snmp_engine,
                community,
                transport,
                context,
                ObjectType(ObjectIdentity(oid_to_walk)),
                lexicographicMode=False
            )

            async for errorIndication, errorStatus, errorIndex, varBinds in objects_to_walk:
                if errorIndication:
                    return [f"Error: {errorIndication}"] # Original behavior
                elif errorStatus:
                    return [f"SNMP Error: {errorStatus.prettyPrint()} at {errorIndex and varBinds[int(errorIndex) - 1][0] or '?'}"] # Original behavior
                else:
                    for oid, value in varBinds:
                        symbolic_oid = resolve_oid(oid, mib_view)
                        formatted_value = format_raw_values(value, type(value).__name__.upper())
                        result.append(f"{symbolic_oid} = {formatted_value}")

    end_time = time.time()
    print(f"Elapsed time: {end_time - start_time:.2f} seconds")
    print(f"SNMP {action_description} completed. Processed {len(result)} entries (data/messages).")
    return result