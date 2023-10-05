#!/usr/bin/python3

def add_all(*args):

    total = 0
    for arg in args:
        total += int(arg)
    return total

if __name__ == "__main__":
    import sys

    total = add_all(*sys.argv[1:])
    print("{}".format(total))
