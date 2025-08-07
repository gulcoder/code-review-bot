# test_change.py

import subprocess
import os

def bad_function():
    subprocess.call("ls -l", shell=True)  # bör ändras till lista och utan shell=True

bad_function()

print("Detta är en teständring som boten borde refaktorera.")
