#!/usr/bin/python3

import subprocess
import os
import sys


def run_pyside6_rcc(resource_file, output_file):
    
    """
    Run pyside6-rcc on the specified resource file.
    Args:
        resource_file (str): Path to the .qrc resource file
        output_file (str): Path for the output Python file
    Returns:
        bool: True if successful, False otherwise
    """

    # Validate input file
    if not os.path.exists(resource_file):
        print(f"Error: Resource file '{resource_file}' not found.")
    if not resource_file.lower().endswith('.qrc'):
        print(f"Warning: Resource file '{resource_file}' doesn't have .qrc extension.")

    # Construct the command
    cmd = ["pyside6-rcc", resource_file, "-o", output_file]
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    try:
        # Execute the command
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print(f"Successfully compiled {resource_file} to {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error running pyside6-rcc: {e}")
        if e.stderr:
            print(f"Error output: {e.stderr}")
    except FileNotFoundError:
        print("Error: pyside6-rcc command not found. Make sure PySide6 is installed.")
        print("You can install it with: pip install pyside6")


if __name__ == "__main__":
    run_pyside6_rcc("assets/text.qrc", "gi_loadouts/face/rsrc/font/text.py")
    run_pyside6_rcc("assets/arti.qrc", "gi_loadouts/face/rsrc/arti/__init__.py")
    run_pyside6_rcc("assets/back.qrc", "gi_loadouts/face/rsrc/char/back.py")
    run_pyside6_rcc("assets/wish.qrc", "gi_loadouts/face/rsrc/char/wish.py")
    run_pyside6_rcc("assets/data.qrc", "gi_loadouts/face/rsrc/data/__init__.py")
    run_pyside6_rcc("assets/face.qrc", "gi_loadouts/face/rsrc/char/face.py")
    run_pyside6_rcc("assets/icon.qrc", "gi_loadouts/face/rsrc/font/icon.py")
    run_pyside6_rcc("assets/rare.qrc", "gi_loadouts/face/rsrc/rare/__init__.py")
    run_pyside6_rcc("assets/name.qrc", "gi_loadouts/face/rsrc/char/name.py")
    run_pyside6_rcc("assets/pmon.qrc", "gi_loadouts/face/rsrc/pmon/__init__.py")
    run_pyside6_rcc("assets/weap.qrc", "gi_loadouts/face/rsrc/weap/__init__.py")
    run_pyside6_rcc("assets/vson.qrc", "gi_loadouts/face/rsrc/vson/__init__.py")
