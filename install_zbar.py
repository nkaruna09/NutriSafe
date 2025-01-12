import os
import subprocess
import sys

def install_zbar():
    # Check if zbar is installed (for Ubuntu/Debian systems)
    try:
        subprocess.run(['dpkg', '-l', 'libzbar0'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("zbar is already installed.")
    except subprocess.CalledProcessError:
        print("zbar not found. Installing...")
        try:
            # Installing zbar on Ubuntu/Debian-based systems
            subprocess.run(['sudo', 'apt-get', 'update'], check=True)
            subprocess.run(['sudo', 'apt-get', 'install', 'libzbar0', '-y'], check=True)
            print("zbar installed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error installing zbar: {e}")
            sys.exit(1)

