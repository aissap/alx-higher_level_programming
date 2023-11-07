#!/usr/bin/python3
"""Defines a file-writing function."""


def write_file(filename="", text=""):
    """Write a string to text file.
    Args:
        filename: The name of the file to write.
        written_char: The text to write to the file.
    Returns:
        The number of characters written.
    """

    with open(filename, 'w', encoding='utf-8') as file:
        written_char = file.write(text)
    return (written_char)
