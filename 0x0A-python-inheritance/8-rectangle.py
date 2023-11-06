#!/usr/bin/python3
"""defines a class rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class representing a rectangle.
    """

    def __init__(self, width, height):
        """
        Initialize a rectangle.
        Args:
            width : The width of the rectangle.
            height : The height of the rectangle."""
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)
