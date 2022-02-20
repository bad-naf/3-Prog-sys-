import os


flags = os.O_NONBLOCK
r, w = os.pipe2(flags)

pid = os.fork()


if pid > 0:

	os.close(r)

	print("Parent process is writing")
	text = b"Hello child process"
	os.write(w, text)
	print("Written text:", text.decode())

	
else:

	os.close(w)

	print("\nChild Process is reading")
	r = os.fdopen(r)
	print("Read text:", r.read())
