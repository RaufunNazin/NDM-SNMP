import re
import io

with open('test.txt', 'r') as file:
    text = file.read()
    
def parse_mac_table_vsol(text):
    print("[+] Parsing MAC table for VSOL vendor...")

    mac_entries = []
    line_pattern = re.compile(
        r"([0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4})\s+"  # MAC
        r"(\d+)\s+"                                    # VLAN
        r"(\w+)\s+"                                    # Type (Dynamic)
        r"(\S+)"                                       # Port
        r"(?:\s+\S+)*",                                # Ignore trailing fields
        re.IGNORECASE
    )

    text_stream = io.StringIO(text)
    line_num = 0

    for line in text_stream:
        line_num += 1
        line = line.strip()
        if not line:
            continue  # skip blank or whitespace-only lines

        parts = line.split()
        if len(parts) == 0:
            continue  # extra guard, though usually not needed

        if re.match(r"^[0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4}$", parts[0], re.IGNORECASE):
            match = line_pattern.match(line)
            if match:
                raw_mac, vlan, _type, raw_port = match.groups()
                clean_mac = raw_mac.replace('.', '').upper()
                mac = ':'.join([clean_mac[k:k+2] for k in range(0, 12, 2)])

                port = raw_port
                port_match = re.match(r'\w+(\d+)/(\d+):(\d+)', raw_port)
                if port_match:
                    port = f"{port_match.group(1)}/{port_match.group(2)}/{port_match.group(3)}"

                mac_entries.append({
                    'mac': mac,
                    'vlan': int(vlan),
                    'port': port
                })
            else:
                print(f"[-] Line {line_num} did not match pattern: '{line}'")

    print(f"[+] Parsed {len(mac_entries)} MAC entries.")
    return mac_entries
    
if __name__ == "__main__":
    mac_entries = parse_mac_table_vsol(text)
    for entry in mac_entries:
        print(entry)