def get_epon_device_ids(device_id):
    # Extract the device_id parts (assuming it is a 32-bit number represented as an integer)
    olt_device = (device_id >> 24) & 0xFF  # Extract the first byte for OLT Device (8-bit)
    card = (device_id >> 16) & 0xFF         # Extract the second byte for Card (8-bit)
    pon_port = (device_id >> 8) & 0xFF      # Extract the third byte for Pon Port (8-bit)
    onu_num = device_id & 0xFF              # Extract the fourth byte for ONU Number (8-bit)
    
    return {
        "OLT Device": olt_device,
        "Card": card,
        "Pon Port": pon_port,
        "ONU Number": onu_num
    }

# Example: The given value "38285328" would be parsed as follows:
device_id = 21499921
ids = get_epon_device_ids(device_id)
print(ids)
print(device_id & 0xFF)