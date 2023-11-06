#!/usr/bin/python3
"""defines a classand inherited checking function"""


def is_kind_of_class(obj, a_class):
    """
    If obj is exactly an instance or inherited instance  of a_class it returns True otherwise False.
    Args:
        obj : The object to check.
        a_class : The class to compare against.
    """
    if isinstance(obj, a_class):
        return (True)
    return (False)
