#!/usr/bin/python3
'''Defines a Square class'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''a geometric square.'''

    def __init__(self, size, x=0, y=0, id=None):
        '''
        Square constructor.

        Args:
            size : Size of the square.
            x : X-coordinate of the square's position.
            y : Y-coordinate of the square's position.
            id : Identifier for the square.
        '''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''String of the Square instance'''

        return "[Square] ({}) {}/{} - {}". \
            format(type(self).__name__, self.id, self.x, self.y, self.width)
