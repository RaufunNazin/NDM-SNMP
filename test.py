import re
import io

with open('test.txt', 'r') as file:
    text = file.read()
    
def parse_mac_table_vsol(text):
    print("[+] Parsing MAC table for VSOL vendor...")

    mac_entries = []
    text_stream = io.StringIO(text)
    line_num = 0

    for line in text_stream:
        line_num += 1
        line = line.strip()
        if not line:
            continue  # skip blank lines

        parts = line.split()
        # We expect at least 4 mandatory parts (MAC, VLAN, Type, Port)
        if len(parts) < 4:
            continue

        # Check if the first part matches MAC format
        if re.match(r"^[0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4}$", parts[0], re.IGNORECASE):
            raw_mac = parts[0]
            vlan = parts[1]
            _type = parts[2]
            raw_port = parts[3]

            clean_mac = raw_mac.replace('.', '').upper()
            mac = ':'.join([clean_mac[k:k+2] for k in range(0, 12, 2)])

            port = raw_port
            port_match = re.match(r'\w+(\d+)/(\d+):(\d+)', raw_port)
            if port_match:
                port = f"{port_match.group(1)}/{port_match.group(2)}/{port_match.group(3)}"

            # gem_index, gem_id, info are optional and can be present at positions 4,5,6+
            gem_index = int(parts[4]) if len(parts) > 4 and parts[4].isdigit() else None
            gem_id = int(parts[5]) if len(parts) > 5 and parts[5].isdigit() else None
            info = " ".join(parts[6:]) if len(parts) > 6 else None

            mac_entries.append({
                'mac': mac,
                'vlan': int(vlan),
                'type': _type,
                'port': port,
                'gem_index': gem_index,
                'gem_id': gem_id,
                'info': info,
            })
        else:
            print(f"[-] Line {line_num} does not start with a MAC address: '{line}'")

    print(f"[+] Parsed {len(mac_entries)} MAC entries.")
    return mac_entries
    
if __name__ == "__main__":
    mac_entries = parse_mac_table_vsol(text)
    for entry in mac_entries:
        print(entry)