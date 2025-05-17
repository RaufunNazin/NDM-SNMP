import asyncio
from pysnmp.hlapi.v3arch.asyncio import *
import os
from dotenv import load_dotenv
import argparse
from utils import snmp_walk, parse_onu_data, insert_into_db
import cx_Oracle
import json

load_dotenv()

# SNMP target settings
target_ip = os.getenv("TARGET_IP")
community_string = os.getenv("COMMUNITY_STRING")
oid_to_walk = os.getenv("OID_TO_WALK")
port = int(os.getenv("PORT", 161))
snmp_version = 0 if(os.getenv("SNMP_VERSION") == "1") else 1 # 0 = SNMPv1, 1 = SNMPv2c
snmp_timeout = int(os.getenv("SNMP_TIMEOUT", 3))
snmp_retries = int(os.getenv("SNMP_RETRIES", 3))
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")
db_sid = os.getenv("DB_SID")
instant_client= os.getenv("INSTANT_CLIENT_LOC")

if not target_ip or not community_string or not oid_to_walk:
    raise ValueError("Please set TARGET_IP, COMMUNITY_STRING, and OID_TO_WALK in the .env file.")
if not snmp_version in [0, 1]:
    raise ValueError("Please set SNMP_VERSION to 1 for SNMPv1 or 2 for SNMPv2c in the .env file.")

# Initialize Oracle client
cx_Oracle.init_oracle_client(lib_dir=instant_client)

# Run and display
async def main():
    parser = argparse.ArgumentParser(description='Process ONU data from SNMP output and insert into database')
    parser.add_argument('-d', '--dry-run', action='store_true', help='Parse data but do not insert into database')
    args = parser.parse_args()
    print("Running SNMP walk...")
    print(f"Target IP: {target_ip}")
    print(f"Community String: {community_string}")
    print(f"OID to walk: {oid_to_walk}")
    print(f"SNMP Version: {'SNMPv1' if snmp_version == 0 else 'SNMPv2c'}")
    print(f"Timeout: {snmp_timeout} seconds")
    print(f"Retries: {snmp_retries}")
    snmp_output = await snmp_walk(target_ip, community_string, oid_to_walk, port, snmp_version, snmp_timeout, snmp_retries)
    
    snmp_data_str = "\n".join(snmp_output)
    
    output_file = 'snmp_output.txt'
    with open(output_file, 'w') as f:
        f.write(snmp_data_str)
        f.close()
    print(f"SNMP output saved to {output_file}")
    print("Parsing SNMP output...")
    
    # Parse the SNMP output
    parsed_snmp_output = parse_onu_data(snmp_data_str)
    parsed_output_file = 'parsed_snmp_output.txt'
    with open(parsed_output_file, 'w') as f:
        f.write(json.dumps(parsed_snmp_output, indent=2, default=str))
        f.close()
    print(f"Parsed SNMP output saved to {parsed_output_file}")
    print(f"Parsed {len(parsed_snmp_output)} ONU devices from SNMP output.")

    # Insert into database unless dry run is specified
    if not args.dry_run:
        insert_into_db(parsed_snmp_output, target_ip, db_host, db_port, db_user, db_pass, db_sid)
    else:
        print("Dry run mode: Data not inserted into database")

if __name__ == "__main__":
    asyncio.run(main())
