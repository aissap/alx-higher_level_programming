#!/usr/bin/python3
"""Defines a text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """Inserts text after each line containing a specified string in a file.
    Args:
        filename (str): The name of the file.
        search_string (str): The string to look for in each line.
        new_string: The string to insert after the target string.
    """
    modified_content = ""

    with open(filename) as file:
        for line in file:
            modified_content += line

            if search_string in line:
                modified_content += new_string

    with open(filename, "w") as file:
        file.write(modified_content)
