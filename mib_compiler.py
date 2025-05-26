import argparse
import os
import logging
from pysmi import debug
from pysmi.reader import FileReader
from pysmi.writer import PyFileWriter
from pysmi.parser import SmiStarParser
from pysmi.codegen import PySnmpCodeGen
from pysmi.compiler import MibCompiler
from enums import MIBS, COMPILED_MIBS

def setup_logging(debug_mode):
    log_file = 'pysmi_debug.log'
    logger = logging.getLogger('pysmi')
    logger.setLevel(logging.DEBUG if debug_mode else logging.INFO)
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG if debug_mode else logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    if debug_mode:
        debug.setLogger(debug.Debug('all'))

def main(debug_mode):
    setup_logging(debug_mode)

    source_mib_dir = MIBS
    output_mib_dir = COMPILED_MIBS
    os.makedirs(output_mib_dir, exist_ok=True)

    mib_compiler = MibCompiler(
        SmiStarParser(),
        PySnmpCodeGen(),
        PyFileWriter(output_mib_dir)
    )
    mib_compiler.add_sources(FileReader(source_mib_dir))

    mib_files = [f for f in os.listdir(source_mib_dir) if os.path.isfile(os.path.join(source_mib_dir, f))]
    mib_names = [os.path.splitext(f)[0] for f in mib_files]

    print(f"Found {len(mib_names)} MIB files to compile")

    dependencies = ['SNMPv2-SMI', 'SNMPv2-TC', 'SNMPv2-CONF', 'SNMPv2-MIB', 'IF-MIB', 'BRIDGE-MIB', 'RFC-1212']

    print("First compiling dependencies...")
    for dep in dependencies:
        if dep in mib_names:
            try:
                result = mib_compiler.compile(dep, noDeps=False, rebuild=True)
                print(f"Compiled {dep}: {result.get(dep, 'unknown result')}")
            except Exception as e:
                print(f"Error compiling dependency {dep}: {e}")

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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compile MIB files with optional debug logging")
    parser.add_argument('-d', '--debug', action='store_true', help='Enable debug mode with detailed logging')

    args = parser.parse_args()
    main(args.debug)
