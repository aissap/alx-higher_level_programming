#!/usr/bin/python3
"""defines an int addition"""


def add_integer(a, b=98):
    """
    Adds two integers.
    Returns:
        int: The addition of a and b.
    Raises:
        TypeError: If a or b is not an integer or float.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
