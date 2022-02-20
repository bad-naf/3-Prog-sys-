import signal, os

def handler(signum, frame):
    print('Signal handler called with signal', signum)
    raise OSError("Couldn't open device!")

signal.signal(signal.SIGALRM, handler)
signal.alarm(5)

fd = os.open('/dev/ttyS0', os.O_RDWR)

signal.alarm(0)