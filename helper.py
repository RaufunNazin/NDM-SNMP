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


async def get_olt_information(target_ip, community_string, port, version, retries, timeout, branch, brand, onu_index_str, card_id):
    """
    Perform an SNMP walk or get operation to retrieve OLT information.
    Returns all resolved OIDs and values as strings.
    """
    result = []
    start_time = time.time()

    # Load MIBs once (this can be further memoized)
    mib_builder = load_mibs()
    mib_view = view.MibViewController(mib_builder)

    # Prepare OID
    if onu_index_str:
        index = encode_index_from_string(onu_index_str, brand, card_id)
        oid_to_query = f'{oid_dictionary[branch][brand]}.{index}'
    else:
        oid_to_query = oid_dictionary[branch][brand]

    # SNMP Session
    snmp_engine, community, transport, context = await get_snmp_session(
        target_ip, port, community_string, version, timeout, retries
    )

    print(f"{'Starting SNMP get' if onu_index_str else 'Starting SNMP walk'} for OID: {oid_to_query}")

    if onu_index_str:
        # Single SNMP get
        errorIndication, errorStatus, errorIndex, varBinds = await get_cmd(
            snmp_engine,
            community,
            transport,
            context,
            ObjectType(ObjectIdentity(oid_to_query))
        )

        if errorIndication:
            return [f"Error: {errorIndication}"]
        elif errorStatus:
            return [f"SNMP Error: {errorStatus.prettyPrint()} at {errorIndex and varBinds[int(errorIndex) - 1][0] or '?'}"]

        for oid, value in varBinds:
            symbolic_oid = resolve_oid(oid, mib_view)
            formatted_value = format_raw_values(value, type(value).__name__.upper())
            result.append(f"{symbolic_oid} = {formatted_value}")
    else:
        # SNMP walk
        objects = walk_cmd(
            snmp_engine,
            community,
            transport,
            context,
            ObjectType(ObjectIdentity(oid_to_query)),
            lexicographicMode=False
        )

        async for errorIndication, errorStatus, errorIndex, varBinds in objects:
            if errorIndication:
                return [f"Error: {errorIndication}"]
            elif errorStatus:
                return [f"SNMP Error: {errorStatus.prettyPrint()} at {errorIndex and varBinds[int(errorIndex) - 1][0] or '?'}"]
            else:
                for oid, value in varBinds:
                    symbolic_oid = resolve_oid(oid, mib_view)
                    formatted_value = format_raw_values(value, type(value).__name__.upper())
                    result.append(f"{symbolic_oid} = {formatted_value}")

    end_time = time.time()
    print(f"Elapsed time: {end_time - start_time:.2f} seconds")
    print(f"SNMP {'get' if onu_index_str else 'walk'} completed. Retrieved {len(result)} OIDs.")
    return result