#!/usr/bin/python3
def uppercase(s):
    for char in s:
        if ord(char) >= 97 and ord(char) <= 122:
            c = chr(ord(char) - 32)
        print("{}".format(char), end="")
    print("")
