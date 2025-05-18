# Function to decode EPON device index
def decode_gpon_device_index(device_id):
    # Extract the raw bytes
    slot = (device_id >> 24) & 0xFF
    pon = (device_id >> 8) & 0xFF
    onu = device_id & 0xFF

    return {
        'SLOT_ID': slot - 1 if slot > 0 else 0,
        'PON_ID': pon - 6,
        'ONU_ID': onu,
    }
    
print(decode_gpon_device_index(16779012))