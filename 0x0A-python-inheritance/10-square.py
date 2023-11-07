#!/usr/bin/python3
"""defines a  subclass Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """representing a square."""

    def __init__(self, size):
        """
        Initialize a square.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)
