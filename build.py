#!/usr/bin/env python3

import sys
import os
import subprocess

# Install dependencies
def install_dependencies():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

# Run the application
def run_app():
    subprocess.check_call([sys.executable, "SMT1.py"])

if __name__ == "__main__":
    install_dependencies()
    run_app()
