#!/usr/bin/python3
"""Rectangle Module"""


class Rectangle:
    """A 2d polygon with four perpendicular sides
    """
    def __init__(self, width=0, height=0):
        """Initializes a Rectangle instance.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width of a Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of a Rectangle instance."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Retrives the height of a Rectangle instance"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height of a Rectangle instance"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
