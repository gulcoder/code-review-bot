import subprocess
import logging  # Importerat men används inte

def dangerous_function():
    # Osäkert subprocess-anrop med shell=True (kan förbättras)
    subprocess.call("ls -l", shell=True)

def duplicate_code():
    # Kopia av dangerous_function, onödig duplicering
    subprocess.call("ls -l", shell=True)

def redundant_function():
    # Onödig if-sats som alltid är True
    if True:
        print("This is redundant")

if __name__ == "__main__":
    dangerous_function()
    duplicate_code()
    redundant_function()
