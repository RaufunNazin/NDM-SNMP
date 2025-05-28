import re

with open('test.txt', 'r') as file:
    text = file.read()
    
def parse_text(text):
    lines = text.strip().splitlines()
    # print(lines)
    for line_num, line in enumerate(lines):
        line = line.strip()
        
        # Skip empty or non-data lines
        mac_pattern = re.compile(r"^([0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4})\s+(\d+)\s+\w+\s+(\S+)\s+\d+\s+\d+\s+\w+$")
        if not line or not mac_pattern.match(line.strip()):
            continue
        else:
            print(lines[line_num])
    
if __name__ == "__main__":
    parse_text(text)