#!/usr/bin/python3

import sys


def print_args():
    argc = len(sys.argv) - 1

    print("{} argument{}{}".format(
        argc, "s" if argc != 1 else "", ":" if argc else "."))

    for i in range(1, argc + 1):
        print("{}: {}".format(i, sys.argv[i]))


if __name__ == "__main__":
    print_args()
