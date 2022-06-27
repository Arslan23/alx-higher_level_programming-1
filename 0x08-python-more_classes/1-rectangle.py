#!/usr/bin/python3
"""Module 0-rectangle
Defines an empty Rectangle class.
"""


class Rectangle:
    """Represent a rectangle."""
    __init__(self, width=0, height=0):
        ''' Init new Rectangle
        Args: 
            width: int
            height: int
        '''
        self.__width = width
        self.__height = height

    @property
    def width(self):
        '''Get width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Set width
        Args:
            value: int, value of width
        '''
        try:
            if isinstance(value, int):
                if value <= 0:
                    raise ValueError("width must be >= 0")
                else:
                    self.__width = value
            else:
                raise TypeError("width must be an integer")

    @property
    def height(self):
        '''Get height'''
        return self.__width

    @height.setter
    def height(self, value):
        '''Set height
        Args: 
            value: int, value of height
        '''
        try:
            if isinstance(value, int):
                if value <= 0:
                    raise ValueError("height must be >= 0")
                else:
                    self.__height = value
            else:
                raise TypeError("height must be an integer")
