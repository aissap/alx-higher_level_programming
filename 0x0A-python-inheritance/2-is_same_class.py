#!/usr/bin/python3
"""defines a class checking function"""


def is_same_class(obj, a_class):
    """
    If obj is exactly an instance of a_class it returns True otherwise False.
    Args:
        obj : The object to check.
        a_class : The class to compare against.
    """
    if type(obj) == a_class:
        return (True)
    return (False)
