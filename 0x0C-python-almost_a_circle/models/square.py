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

    @property
    def size(self):
        """Size of this square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def  update(self, *args, **kwargs):
        """Updates Square attributes via no-keyword or keyword arguments."""
        attrs = ["id", "size", "x", "y"]

        if args and len(attrs) > 0:
            for i, arg in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
