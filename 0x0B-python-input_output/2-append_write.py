#!/usr/bin/python3
"""Defines a file append function"""


def append_write(filename="", text=""):
    """Append a string into the end of a file txt"""
    with open(filename, 'a', encoding='utf-8') as file:
        added_char = file.write(text)
    return (added_char)
