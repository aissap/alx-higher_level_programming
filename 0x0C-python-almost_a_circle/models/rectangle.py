#!/usr/bin/python3
'''Module for rectangle class'''
from models.base import Base


class Rectangle(Base):
    '''Rectangle class: Represents a geometric rectangle.'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''
        Rectangle constructor.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int): X-coordinate of the rectangle's position.
            y (int): Y-coordinate of the rectangle's position.
            id (int): Identifier for the rectangle.
        '''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        '''Getter for the width of this rectangle.'''
        return self.__width

    @width.setter
    def width(self, value):
        '''
        Setter for the width of this rectangle.

        Args:
            value (int): New width value.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        '''Getter for the height of this rectangle.'''
        return self.__height

    @height.setter
    def height(self, value):
        '''
        Setter for the height of this rectangle.

        Args:
            value (int): New height value.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        '''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        '''Getter for the x-coordinate of this rectangle.'''
        return self.__x

    @x.setter
    def x(self, value):
        '''
        Setter for the x-coordinate of this rectangle.

        Args:
            value (int): New x-coordinate value.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        '''
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''Getter for the y-coordinate of this rectangle.'''
        return self.__y

    @y.setter
    def y(self, value):
        '''
        Setter for the y-coordinate of this rectangle.

        Args:
            value (int): New y-coordinate value.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        '''
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''Calculate the area of the rectangle.'''
        return self.__width * self.__height

    def display(self):
        '''display the rectangle with # characters.'''
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        '''the __str__ method represents the object as a string.'''
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height
        )

    def update(self, *args):
        '''
        Update attributes of the Rectangle instance.'''
        attributes = ["id", "width", "height", "x", "y"]

        for i, arg in enumerate(args):
            setattr(self, attributes[i], arg)
