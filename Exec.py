import os
import sys

def exec_family():
	rc = os.fork()

	if rc < 0:
		print("fork failed")

	if rc > 0:
		os.wait()

	if rc == 0:

		#os.execl("/bin/ls", "ls", *sys.argv)
		#os.execlp("ls", "ls", *sys.argv)
		os.execle("/bin/ls", "ls", {})
		#os.execv("/bin/ls", sys.argv)
		#os.execvp("ls", sys.argv)
		#os.execvpe("ls", sys.argv, {})



exec_family()