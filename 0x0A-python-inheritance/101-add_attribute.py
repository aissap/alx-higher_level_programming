#!/usr/bin/python3
"""defines a function wich adds attributes to objects."""


def add_attribute(obj, attribute, value):
    """
    Add a new attribute to an object.
    Args:
        obj : The object to add the attribute to.
        attribute : The name of the attribute.
        value : The value of the attribute.
    Raises:
        TypeError: If the object can't have new attributes.
    """
    if not hasattr(obj, '__dict__') or hasattr(obj, '__class__'):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")
