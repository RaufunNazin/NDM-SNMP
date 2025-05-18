from enums import SLOT_ID, PON_ID, ONU_ID

# Function to decode EPON device index
def decode_cdata_epon(device_id):
    # Extract the raw bytes
    slot = (device_id >> 24) & 0xFF
    pon = (device_id >> 8) & 0xFF
    onu = device_id & 0xFF

    return {
        SLOT_ID: slot,
        PON_ID: (pon // 16) + 1,
        ONU_ID: onu,
    }
    
# Function to decode EPON device index
def decode_cdata_gpon(device_id):
    # Extract the raw bytes
    slot = (device_id >> 24) & 0xFF
    pon = (device_id >> 8) & 0xFF
    onu = device_id & 0xFF

    return {
        SLOT_ID: slot - 1 if slot > 0 else 0,
        PON_ID: pon - 6,
        ONU_ID: onu,
    }