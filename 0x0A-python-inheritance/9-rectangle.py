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
        self.__width = width
        self.__height = height
        self.integer_validator("height", height)
        self.integer_validator("width", width)

    def area(self):
        """Returns:
            int: The area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns:
            str: A string representation of the rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
