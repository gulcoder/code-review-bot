# test_change.py

import subprocess

def bad_function():
    # Osäker användning av subprocess med shell=True
    subprocess.call("ls -l", shell=True)

if __name__ == "__main__":
    bad_function()
    print("Detta är en teständring som boten borde refaktorera.")

