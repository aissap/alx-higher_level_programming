#!/usr/bin/python3
"""Base module"""


class Base:
    """Representation of the Base class"""

    __nb_objects = 0

    def __init__(self, id = None):
        """constructor"""
        if id != None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
