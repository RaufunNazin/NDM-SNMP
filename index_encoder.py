import re
from enums import EPON_LOWER, GPON_LOWER, CDATA

def _parse_interface_string(interface_string: str):
    """
    Parses an interface string like "epon0/0/1/24" or "gpon0/2/4/14".
    The format is <type><frame_id>/<slot_id>/<pon_id>/<onu_id>.

    Args:
        interface_string (str): The interface string.

    Returns:
        tuple: (type_str, frame_id, slot_id, pon_id, onu_id)
               type_str is "epon" or "gpon".
               Others are integers.
    Raises:
        ValueError: if the string format is invalid.
    """
    match = re.match(r"^(epon|gpon)(\d+)/(\d+)/(\d+)/(\d+)$", interface_string)
    if not match:
        raise ValueError(
            f"Invalid interface string format: {interface_string}. "
            "Expected format like 'epon0/0/1/24' or 'gpon0/2/4/14'."
        )
    
    type_str = match.group(1)
    frame_id = int(match.group(2))
    slot_id = int(match.group(3))
    pon_id = int(match.group(4))
    onu_id = int(match.group(5))
    
    return type_str, frame_id, slot_id, pon_id, onu_id

def encode_cdata_epon_index(slot_id: int, pon_id: int, onu_id: int) -> int:
    """
    Encodes CDATA EPON slot, PON, and ONU IDs into a device_id integer.
    This is the reverse of the decoding logic in decode_cdata_epon.

    Args:
        slot_id (int): The logical slot ID (typically 0-indexed).
                       Corresponds to the raw slot byte.
        pon_id (int): The logical PON ID (1-indexed, as per decoder output `(raw_pon_byte // 16) + 1`).
        onu_id (int): The logical ONU ID (0-indexed). Corresponds to the raw ONU byte.

    Returns:
        int: The encoded device_id.
    Raises:
        ValueError: if input IDs are out of their valid range.
    """
    if not (0 <= slot_id <= 255):
        raise ValueError(f"EPON Slot ID {slot_id} out of range [0, 255].")
    # For EPON, decoded PON ID = (raw_pon_byte // 16) + 1.
    # So, raw_pon_byte = (pon_id - 1) * 16.
    # raw_pon_byte must be <= 255. So (pon_id - 1) * 16 <= 255
    # pon_id - 1 <= 255/16 = 15.9375 => pon_id - 1 <= 15 => pon_id <= 16.
    if not (1 <= pon_id <= 16):
        raise ValueError(f"EPON PON ID {pon_id} out of range [1, 16].")
    if not (0 <= onu_id <= 255):
        raise ValueError(f"EPON ONU ID {onu_id} out of range [0, 255].")

    raw_slot_byte = slot_id
    raw_pon_byte = (pon_id - 1) * 16
    raw_onu_byte = onu_id
    
    device_id = (raw_slot_byte << 24) | (raw_pon_byte << 8) | raw_onu_byte
    return device_id

def encode_cdata_gpon_index(slot_id: int, pon_id: int, onu_id: int) -> int:
    """
    Encodes CDATA GPON slot, PON, and ONU IDs into a device_id integer.
    This is the reverse of the decoding logic in decode_cdata_gpon.

    Args:
        slot_id (int): The logical slot ID (0-indexed, as per decoder output `raw_slot_byte - 1`).
        pon_id (int): The logical PON ID (as per decoder output `raw_pon_byte - 6`).
        onu_id (int): The logical ONU ID (0-indexed). Corresponds to the raw ONU byte.

    Returns:
        int: The encoded device_id.
    Raises:
        ValueError: if input IDs are out of their valid range.
    """
    # For GPON, decoded SLOT_ID = raw_slot_byte - 1 (assuming raw_slot_byte > 0 for physical slots).
    # So, raw_slot_byte = slot_id + 1.
    # raw_slot_byte must be <= 255. So slot_id + 1 <= 255 => slot_id <= 254.
    # Assuming slot_id is 0-indexed and non-negative.
    if not (0 <= slot_id <= 254):
        raise ValueError(f"GPON Slot ID {slot_id} out of range [0, 254].")
    
    # For GPON, decoded PON_ID = raw_pon_byte - 6.
    # So, raw_pon_byte = pon_id + 6.
    # raw_pon_byte must be <= 255. So pon_id + 6 <= 255 => pon_id <= 249.
    if not (0 <= pon_id <= 249):
        raise ValueError(f"GPON PON ID {pon_id} out of range [0, 249].")
        
    if not (0 <= onu_id <= 255):
        raise ValueError(f"GPON ONU ID {onu_id} out of range [0, 255].")

    raw_slot_byte = slot_id + 1 
    raw_pon_byte = pon_id + 6
    raw_onu_byte = onu_id
    
    device_id = (raw_slot_byte << 24) | (raw_pon_byte << 8) | raw_onu_byte
    return device_id

def encode_index_from_string(interface_string: str, brand) -> int:
    """
    Encodes an interface string (e.g., "epon0/0/1/24" or "gpon0/2/4/14") 
    into a device_id integer. The frame_id part of the string is parsed but
    not used in generating the device_id, based on the reversal of the
    provided decoder functions.

    Args:
        interface_string (str): The interface string.
        brand (str): The brand of the device (e.g., "CDATA").

    Returns:
        int: The encoded device_id.
    Raises:
        ValueError: if the string format is invalid or type is unknown.
    """
    type_str, _frame_id, slot_id, pon_id, onu_id = _parse_interface_string(interface_string)
    # _frame_id is parsed but not used in the device_id encoding itself,
    # as per the structure of the original decoders.
    
    if type_str == EPON_LOWER:
        if brand == CDATA:
            return encode_cdata_epon_index(slot_id, pon_id, onu_id)
    elif type_str == GPON_LOWER:
        if brand == CDATA:
            return encode_cdata_gpon_index(slot_id, pon_id, onu_id)
    else:
        # This case should ideally be caught by _parse_interface_string's regex
        raise ValueError(f"Unknown interface type: {type_str}")