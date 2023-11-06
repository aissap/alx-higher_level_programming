#!/usr/bin/python3

def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.
    Args:
        obj: The object to look up.

    Returns:
             List of available attributes and methods.

    """
    return dir(obj)
