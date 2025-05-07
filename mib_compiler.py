from pysmi.reader import FileReader
from pysmi.writer import PyFileWriter
from pysmi.parser import SmiStarParser
from pysmi.codegen import PySnmpCodeGen
from pysmi.compiler import MibCompiler
import os
# import logging
# from pysmi import debug

# # Set up logging to a file
# log_file = 'pysmi_debug.log'

# logger = logging.getLogger('pysmi')
# logger.setLevel(logging.DEBUG)

# file_handler = logging.FileHandler(log_file)
# file_handler.setLevel(logging.DEBUG)

# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# file_handler.setFormatter(formatter)

# logger.addHandler(file_handler)

# # Enable all PySMI debug modules (or specify subset)
# debug.set_logger(debug.Debug('all'))

# Define directories
source_mib_dir = 'mibs'
output_mib_dir = 'compiled_mibs'

# Create output directory if it doesn't exist
os.makedirs(output_mib_dir, exist_ok=True)

# Initialize MIB compiler
mib_compiler = MibCompiler(
    SmiStarParser(),
    PySnmpCodeGen(),
    PyFileWriter(output_mib_dir)
)

# Add source directories
mib_compiler.add_sources(FileReader(source_mib_dir))

# Get list of all MIB files in the directory
mib_files = [f for f in os.listdir(source_mib_dir) if os.path.isfile(os.path.join(source_mib_dir, f))]
mib_names = [os.path.splitext(f)[0] for f in mib_files]

print(f"Found {len(mib_names)} MIB files to compile")

# First try to compile the dependencies that ENTITY-MIB needs
dependencies = ['IANA-ENTITY-MIB', 'UUID-TC-MIB', 'SNMP-FRAMEWORK-MIB', 
                'SNMPv2-SMI', 'SNMPv2-TC', 'SNMPv2-CONF', 'SNMPv2-MIB', 'FD-ONU-MIB', 'FD-OLT-MIB', 'FD-SYSTEM-MIB', 'EPON-EOC-MIB']

print("First compiling dependencies...")
for dep in dependencies:
    if dep in mib_names:
        try:
            result = mib_compiler.compile(dep, noDeps=False, rebuild=True)
            print(f"Compiled {dep}: {result.get(dep, 'unknown result')}")
        except Exception as e:
            print(f"Error compiling dependency {dep}: {e}")

# Now compile the rest of the MIBs
print("\nNow compiling remaining MIBs...")
for mib in mib_names:
    if mib not in dependencies:
        try:
            result = mib_compiler.compile(mib, noDeps=False, rebuild=True)
            status = result.get(mib, "unknown")
            print(f"Compiled {mib}: {status}")
        except Exception as e:
            print(f"Error compiling {mib}: {e}")

print(f"\nAll compilations completed. Check {output_mib_dir} for results.")
