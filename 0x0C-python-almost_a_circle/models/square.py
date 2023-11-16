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

    @property
    def size(self):
        '''Getter for the size of the square'''
        return self.width

    @size.setter
    def size(self, value):
        '''Set the size of the square'''
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''Update attributes of the square'''
        attrs = ["id", "size", "x", "y"]
        if args:
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                if key in attrs:
                    setattr(self, key, value)

    def to_dictionary(self):
        '''Return the dictionary'''
        return {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}
