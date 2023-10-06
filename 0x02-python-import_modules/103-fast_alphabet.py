#!/usr/bin/python3

if __name__ == "__main__":
    with open(1, 'w', encoding='utf-8', closefd=False) as stdout:
        stdout.write("#pythoniscool\n")

import string
print(string.ascii_uppercase)
