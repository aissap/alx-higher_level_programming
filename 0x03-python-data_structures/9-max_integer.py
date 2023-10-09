#!/usr/bin/python3
def max_integer(my_list=[]):
    """
    Finds the largest integer in a list.

    Args:
        my_list (list): The list of integers.

    Returns:
        int or None: The largest integer in the list, or None.
    """
    if not my_list:
        return None

    max_value = my_list[0]
    for num in my_list:
        if num > max_value:
            max_value = num

    return max_value
