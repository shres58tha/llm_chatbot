from import_xyz import import_xyz
import_xyz('os')
import_xyz('subprocess')

import os
import subprocess


def is_virtualenv_present():
    # Check for the existence of 'bin' (or 'Scripts' on Windows) and 'lib' directories
    bin_dir = "bin" if os.name != "nt" else "Scripts"
    lib_dir = "lib"
    return os.path.exists(bin_dir) and os.path.exists(lib_dir)

def create_virtualenv(venv_name):
    # Check if virtualenv is installed
    try:
        subprocess.run(["virtualenv", "--version"], capture_output=True, check=True)
    except FileNotFoundError:
        print("virtualenv is not installed. Please install it using 'pip install virtualenv' \n autoinstalling")
        import_xyz("virtualenv")

    # Create the virtual environment
    try:
        subprocess.run(["virtualenv", venv_name], check=True)
        print(f"Virtual environment '{venv_name}' created successfully.")
    except subprocess.CalledProcessError:
        print(f"Failed to create virtual environment '{venv_name}'.")
        
        
if is_virtualenv_present():
    print("Virtual environment is present in the current folder.")
else:
    print("Virtual environment is NOT present in the current folder.")
    venv_name = ""  # Change this to the desired name for your virtual environment
    create_virtualenv(venv_name)