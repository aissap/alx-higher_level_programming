#!/usr/bin/python3
"""Defines an inherited list class"""


class MyList(list):
    """
    A class that inherits from list.
    """

    def print_sorted(self):
        """
        Print the list in sorted (ascending) order.
        """
        print(sorted(self))
