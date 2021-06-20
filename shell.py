import shlex
import signal
import sys


def signal_handler(signum, frame):
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler) 


while True:
	try:
		cmd, *args = shlex.split(input('>>> '))
	except Exception as e:
		continue
	else:
		cmd = cmd + ' ' + ' '.join(args)
		r = exec(cmd)
		if r is not None:
			print(r)

