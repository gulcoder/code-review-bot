import subprocess

def say_hello():
    print("Hello world")
    print("Hello world")  # duplicerad rad

def insecure_call():
    subprocess.call("ls", shell=True)
