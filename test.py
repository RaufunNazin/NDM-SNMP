import re

with open('test.txt', 'r') as file:
    text = file.read()
    
def parse_mac_table_vsol(text):
    print("[+] Parsing MAC table for VSOL vendor...")
    
    mac_entries = []
    lines = text.strip().splitlines()
    
    for line_num, line in enumerate(lines):
        line = line.strip()
        
        # Skip empty or non-data lines
        line_pattern = re.compile(r"^([0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4})\s+(\d+)\s+\w+\s+(\S+)\s+\d+\s+\d+\s+\w+$", re.IGNORECASE)
        if line_pattern.match(line.strip()):
            raw_mac, vlan, raw_port = line_pattern.match(line.strip()).groups()
            
            # Convert MAC to xx:xx:xx:xx:xx:xx
            clean_mac = raw_mac.replace('.', '').upper()
            mac = ':'.join([
                clean_mac[i:i+2] for i in range(0, 12, 2)
            ])

            
            # Extract port details like GPON0/1:18 → 1/18
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
            print(f"[-] Skipping line {line_num + 1}: '{line}' - does not match expected format.")
    
    print(f"[+] Parsed {len(mac_entries)} MAC entries.")
    return mac_entries
    
if __name__ == "__main__":
    print(parse_mac_table_vsol(text))