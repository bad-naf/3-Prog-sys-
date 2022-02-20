import os

def forkAndWait():
	rc = os.fork()

	if rc < 0:
		print("fork failed")

	if rc > 0:
		v = os.wait()
		print("value returned by wait call:", v)
		print("I'm parent and my id is ", os.getpid())
		print("I'm parent and my parent id is", os.getppid())


	if rc == 0:
		print("I'm child and my id is", os.getpid())
		print("I'm child and my parent id is", os.getppid())




forkAndWait()