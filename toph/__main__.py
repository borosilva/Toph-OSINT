from signal import signal, SIGINT
from sys import exit
from toph import app

def handler(signal_received, frame):
    print(' CTRL-C detected. Exiting gracefully')
    exit(0)

if __name__ == "__main__":
    signal(SIGINT, handler)
    app.run()