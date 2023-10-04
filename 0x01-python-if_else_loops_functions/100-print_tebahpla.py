#!/usr/bin/python3

n = 0
for char in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(char - n)), end="")
    n = 32 if n == 0 else 0
