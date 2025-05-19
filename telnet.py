import telnetlib
import time
import re

HOST = "10.254.0.5"
PORT = 1123
USERNAME = "admin"
PASSWORD = "admin"
MORE_PROMPT = b"--More ( Press 'Q' to quit )--"

def detect_prompt(tn):
    tn.write(b"\n")
    time.sleep(1)
    response = tn.read_very_eager()
    lines = response.strip().split(b"\n")
    if lines:
        last_line = lines[-1].strip()
        if last_line.endswith(b"#") or last_line.endswith(b">"):
            return last_line
    raise ValueError("Failed to detect device prompt.")

def send_command_with_prompt_and_pagination(tn, command, prompt, more_prompt=MORE_PROMPT):
    print(f"[+] Sending command: {command}")
    tn.write(command.encode('ascii') + b"\n")
    output = b""
    while True:
        chunk = tn.read_until(more_prompt, timeout=5)
        output += chunk
        if more_prompt in chunk:
            print("[+] More data found, sending SPACE")
            tn.write(b" ")
        else:
            # Ensure final prompt is received
            remaining = tn.read_until(prompt, timeout=10)
            output += remaining
            break
    return output.decode("utf-8", errors="ignore")

def parse_mac_table(text):
    mac_entries = []

    # Skip lines before data starts
    lines = text.strip().splitlines()
    data_lines = [line for line in lines if re.match(r"\s*([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}", line)]

    for line in data_lines:
        # This regex handles flexible spacing and optional numeric fields
        match = re.match(
            r"\s*([0-9A-Fa-f:]{17})\s+"    # MAC
            r"(\d+)\s+"                    # VLAN
            r"(-|\d+)\s+"                  # Sport
            r"(\S+)\s+"                    # Port
            r"(-|\d+)\s+"                  # ONU
            r"(-|\d+)\s+"                  # Gemid
            r"(dynamic|static)",           # MAC-Type
            line
        )
        if match:
            mac, vlan, sport, port, onu, gemid, mac_type = match.groups()
            formatted_port = f"{port}:{onu}" if onu != "-" else port
            mac_entries.append({
                "mac": mac,
                "vlan": int(vlan),
                "port": formatted_port
            })

    return mac_entries

def main():
    try:
        print(f"[+] Connecting to {HOST}:{PORT} ...")
        tn = telnetlib.Telnet(HOST, PORT, timeout=10)
        print("[+] Connected.")

        print("[+] Waiting for username prompt...")
        tn.read_until(b"Username:", timeout=5)
        print("[+] Got username prompt.")
        tn.write(USERNAME.encode("ascii") + b"\n")

        print("[+] Waiting for password prompt...")
        tn.read_until(b"Password:", timeout=5)
        print("[+] Got password prompt.")
        tn.write(PASSWORD.encode("ascii") + b"\n")

        time.sleep(1)  # wait for prompt to appear
        prompt = detect_prompt(tn)
        print(f"[+] Detected prompt: {prompt.decode()}")

        # Enter enable mode
        print("[+] Sending 'enable' command...")
        tn.write(b"enable\n")
        time.sleep(1)

        # Optionally go to config if needed
        tn.write(b"config\n")
        time.sleep(1)
        prompt = detect_prompt(tn)
        print(f"[+] Updated prompt after config: {prompt.decode()}")

        # Run the target command with pagination support
        output = send_command_with_prompt_and_pagination(tn, "show mac-address all", prompt)
        print("\n[+] Full output of 'show mac-address all':\n")

        parsed_output = parse_mac_table(output)
        for entry in parsed_output:
                print(entry)

        print("[+] Session ended.")
        tn.close()

    except Exception as e:
        print("[-] Unexpected error occurred.")
        print(f"[-] Details: {e}")

if __name__ == "__main__":
    main()

