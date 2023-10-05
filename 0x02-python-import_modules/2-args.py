#!/usr/bin/python3
import sys

def print_args():
    argc = len(sys.argv) - 1

    print(f"{argc} argument(s):")

    for i in range(1, argc + 1):
        print(f"{i}: {sys.argv[i]}")

if __name__ == "__main__":
    print_args()
