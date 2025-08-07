# bad_test_change.py

import subprocess

def dangerous_function():
    # Här använder vi shell=True, vilket är en säkerhetsrisk
    subprocess.call("ls -l", shell=True)

def redundant_function():
    if True:
        print("Detta är onödig if-sats")

if __name__ == "__main__":
    dangerous_function()
    redundant_function()
