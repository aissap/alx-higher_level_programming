#!/usr/bin/python3


def say_my_name(first_name, last_name=""):
    """
    Print a name in the format: My name is <first_name> <last_name>
    Args:
        first_name (str): The first name.
        last_name (str): The last name. 

    Raises:
        TypeError: If either first_name or last_name is not a string.
    """
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError("first_name and last_name must be strings")

    print("My name is {} {}".format(first_name, last_name))
