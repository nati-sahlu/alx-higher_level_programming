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
            self.__width = value

        @property
        def height(self):
            """gets the height of the rectangle"""
            return self.__height

        @height.setter
        def height(self, value):
            """sets the heght of the rectangle"""
            self.__height = value

        @property
        def x(self):
            """gets x of this rectangle."""
            return self.__x

        @x.setter
        def x(self, value):
            """sets x of this rectangle."""

            self.__x = value

        @property
        def y(self):
            """gets y of this rectangle."""
            return self.__y

        @y.setter
        def y(self, value):
            """sets y of this rectangle."""
            self.__y = value
