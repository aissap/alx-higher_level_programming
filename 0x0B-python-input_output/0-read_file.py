#!/usr/bin/python3
"""Defines a text file-reading function."""


def read_file(filename=""):
    """Print the contents of a text file to stdout."""
    with open(filename, 'r', encoding="utf-8") as file:
        print(file.read(), end="")
