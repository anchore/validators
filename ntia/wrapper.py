#!/usr/bin/env python3

import sys
import shutil
import subprocess
import os
import argparse

def main():
    # Parse the argument for the extension using the --extension flag
    parser = argparse.ArgumentParser(description="Process stdin and check using ntia-checker.")
    parser.add_argument("--extension", required=True, choices=["rdf", "tag", "json", "xml", "yaml"],
                        help="The format of the input file (e.g., .rdf, .json, etc.)")
    args = parser.parse_args()

    # Define the temporary file name in the local directory
    temp_file_name = f"input_file.{args.extension}"

    # Write the bytes to the local temporary file
    with open(temp_file_name, "wb") as temp_file:
        shutil.copyfileobj(sys.stdin.buffer, temp_file)

    sy = os.system(f"ntia-checker --file {temp_file_name}")
    # Clean up the temporary file after use
    os.remove(temp_file_name)
    sys.exit(os.waitstatus_to_exitcode(sy))

if __name__ == "__main__":
    main()

