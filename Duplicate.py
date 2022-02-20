import os

path = "./alfa.txt"


fd = os.open(path, os.O_WRONLY)

print("Original file descriptor:", fd)

dup_fd = os.dup(fd)

print("Duplicated file descriptor:", dup_fd)


os.close(fd)
os.close(dup_fd)

print("File descriptor duplicated successfully")
