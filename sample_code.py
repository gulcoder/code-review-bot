import subprocess

def complex_function(x):
    if x > 0:
        for i in range(x):
            logging.info(i)
    else:
        logging.info("No numbers")

def insecure_function():
    # Bandit gillar inte detta, risk för command injection
    subprocess.call("ls -l", shell=True)

def another_function():
    # Lite komplexitet med flera villkor
    if True:
        if False:
            logging.info("Unreachable")
        else:
            logging.info("Hello")
