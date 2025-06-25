#!/usr/bin/python3
"""Define a class that is called Rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """class named Rectangle which is subclass of Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """gets width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """"sets width of the rectangle"""
        self.validate("width", value, allow_zero=False)
        self.__width = value

    @property
    def height(self):
        """gets the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the heght of the rectangle"""
        self.validate("height", value, allow_zero=False)
        self.__height = value

    @property
    def x(self):
        """gets x of this rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """sets x of this rectangle."""
        self.validate("x", value, allow_zero=True)
        self.__x = value

    @property
    def y(self):
        """gets y of this rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """sets y of this rectangle."""
        self.validate("y", value, allow_zero=True)
        self.__y = value

    def validate(self, name, value, allow_zero=True):
        '''Method for validating the value.'''
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if allow_zero:
            if value < 0:
                raise ValueError(f"{name} must be >= 0")
        else:
            if value <= 0:
                raise ValueError(f"{name} must be > 0")

    def area(self):
        """Returns the area of the rectangle"""
        return self.width * self.height

    def display(self):
        '''Prints string representation of the rectangle.'''
        char = '\n' * self.y + \
            (' ' * self.x + '#' * self.width + '\n') * self.height
        print(char, end='')

    def __str__(self):
        """Returns string info about this rectangle."""
        return (f"[{type(self).__name__}] ({self.id}) "
                f"{self.x}/{self.y} - {self.width}/{self.height}")

    def update(self, *args):
        """Assigns arguments to attributes in order: id, width, height, x, y"""
        attrs = ['id', 'width', 'height', 'x', 'y']
        for i, arg in enumerate(args):
            if i < len(attrs):
                setattr(self, attrs[i], arg)
