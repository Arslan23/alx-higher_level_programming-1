#!/usr/bin/python3
'''defines a square'''


class Square:
    '''Represent a square'''
    def __init__(self, size=0):
        '''Init new Square

        Args: size:

            size(int) : Size of the new Square
            size must be an integer upper than 0
        '''
        try:
            if not isinstance(size, int):
                raise TypeError("size must be an integer")
            elif size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
