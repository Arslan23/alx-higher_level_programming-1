#!/usr/bin/python3
"""Module 0-rectangle
Defines an empty Rectangle class.
"""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''Public methode area that return the rectangle area
        Return : height * width
        '''
        return self.__height * self.__width

    def perimeter(self):
        '''Public methode perimeter that return the rectangle perimeter
        Return : 0 if height or width less equal 0 , else perimeter
        '''
        if self.__height <= 0 or self.__width <= 0:
            return 0
        else:
            return (self.__height + self.__width) * 2

    def __str__(self):
        '''Methode print Rectangle with #
        Return: representation
        '''
        representation = ""
        if self.__height <= 0 or self.__width <= 0:
            return representation
        for i in range(1, self.__height + 1):
            for j in range(1, self.__width + 1):
                representation = representation + "#"
            representation = representation + "\n"
        return representation

    def __repr__(self):
        '''Methode print Rectangle with #
    Return: (Rectangle) representation'''
        representation = Rectangle()
        if self.__height <= 0 or self.__width <= 0:
            representation = self
        return representation
