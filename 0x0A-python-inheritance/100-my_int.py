#!/usr/bin/python3i
"""defines a class wich inherits from int."""


class MyInt(int):
    """Class representing an integer."""

    def __eq__(self, other):
        """
        Check if the  integer is equal to another integer.
        Returns:True if not equal, False if equal.
        """
        return (self.real != other)

    def __ne__(self, other):
        """
        Check if the intger is not equal to another integer, or equal.
            bool: True if equal, False if not equal."""
        return (self.real == other)
