#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """
    Finds all multiples of 2 in a list.

    Args:
        my_list (list): The list of integers.

    Returns:
        list of bool: A new list containing True for multiples of 2, and False.
    """
    multiples = [num % 2 == 0 for num in my_list]
    return multiples
