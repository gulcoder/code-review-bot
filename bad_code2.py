# bad_code2.py

import subprocess

def list_files():
    subprocess.call("ls -la", shell=True)

def duplicate_code():
    subprocess.call("ls -la", shell=True)

for i in range(0, 10):
    if i % 2 == 0:
        logging.info(i)
    else:
        logging.info(i)
