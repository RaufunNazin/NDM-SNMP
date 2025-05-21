import telnetlib
import time
import re
import argparse
import os
from dotenv import load_dotenv
from onu_scraper import insert_into_db_olt_customer_mac

# Load environment variables from .env file
load_dotenv()

db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")
db_sid = os.getenv("DB_SID")

MORE_PROMPT = b"--More ( Press 'Q' to quit )--"

def detect_prompt(tn):
    tn.write(b"\n")
    time.sleep(1)
    response = tn.read_very_eager()
    lines = response.strip().split(b"\n")
    if lines:
        last_line = lines[-1].strip()
        if b">" in last_line:
            prompt = last_line.split(b">")[0]
            return prompt
    raise ValueError("Failed to detect device prompt.")

def flush_extra_output(tn):
    tn.write(b"\n")
    tn.write(b"\n")
    tn.write(b"\n")
    _ = tn.read_very_eager()  # Discard junk
    
def send_command_with_prompt_and_pagination(tn, command, prompt, more_prompt=MORE_PROMPT):
    print(f"[+] Sending command: {command}")
    
    flush_extra_output(tn)
    time.sleep(1)

    # Send the command
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
            formatted_port = f"{port}/{onu}" if onu != "-" else port
            mac_entries.append({
                "MAC": mac,
                "VLAN": int(vlan),
                "Port": formatted_port
            })

    return mac_entries
        
def main():
    parser = argparse.ArgumentParser(description="Telnet MAC Address Table Fetcher")
    parser.add_argument("-i", required=True, help="Target device IP address")
    parser.add_argument("-p", type=int, default=23, help="Telnet port (default: 23)")
    parser.add_argument("-u", required=True, help="Username for telnet login")
    parser.add_argument("-ps", required=True, help="Password for telnet login")
    parser.add_argument('-d', '--dry-run', action='store_true', help='Parse data but do not insert into database')
    
    args = parser.parse_args()
    
    HOST = args.i
    PORT = args.p
    USERNAME = args.u
    PASSWORD = args.ps
    
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

        # Flush any extra output
        print("[+] Flushing extra output...")
        flush_extra_output(tn)
        print("[+] Flushed extra output.")
        
        # Enter enable mode
        print("[+] Sending 'enable' command...")
        tn.write(b"enable\n")
        time.sleep(1)
        
        # Flush any extra output
        print("[+] Flushing extra output...")
        flush_extra_output(tn)
        print("[+] Flushed extra output.")

        # Optionally go to config if needed
        tn.write(b"config\n")
        time.sleep(1)
        
        # Flush any extra output
        print("[+] Flushing extra output...")
        flush_extra_output(tn)
        print("[+] Flushed extra output.")

        # Run the target command with pagination support
        output = send_command_with_prompt_and_pagination(tn, "show mac-address all", prompt)
        print("\n[+] Full output of 'show mac-address all':\n")
        
        print(output)
        
        print("----------------------------------------------------")

        parsed_output = parse_mac_table(output)
        for entry in parsed_output:
                print(entry)

        print("[+] Session ended.")
        tn.close()
        
        # Insert into database unless dry run is specified
        if not args.dry_run:
            insert_into_db_olt_customer_mac(parsed_output, HOST, db_host, db_port, db_user, db_pass, db_sid)
        else:
            print("Dry run mode: Data not inserted into database")

    except Exception as e:
        print("[-] Unexpected error occurred.")
        print(f"[-] Details: {e}")

if __name__ == "__main__":
    main()

