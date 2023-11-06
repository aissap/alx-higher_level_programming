#!/usr/bin/python3
"""defines an inherited class-checking function"""


def inherits_from(obj, a_class):
    """
    If obj is exactly an  inherited instance
    of a_class it returns True otherwise False.
    Args:
        obj : The object to check.
        a_class : The class to compare with.
    """
    if isinstance(obj, a_class) and type(obj) != a_class:
        return (True)
    return (False)
