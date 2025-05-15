def decode_epon_device_index(device_id):
    # Extract the raw bytes
    slot = (device_id >> 24) & 0xFF
    pon = (device_id >> 8) & 0xFF
    onu = device_id & 0xFF

    return {
        "Slot ID": slot,
        "PON ID": (pon // 16) + 1,
        "ONU ID": onu,
    }


# device_id = 786436
# decoded = decode_epon_device_index(device_id)
# print("Main: epon0/2/1, ONU ID: 20")
# for k, v in decoded.items():
#     print(f"{k}: {v}")