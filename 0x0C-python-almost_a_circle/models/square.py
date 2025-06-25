#!/usr/bin/python3
"""Define a class called Square inhirted from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Constructer"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns string info about this square."""
        return '[{}] ({}) {}/{} - {}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width)
