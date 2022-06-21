#!/usr/bin/python3

class Square:
    def __init__(self,size = 0):
        try:
            self.size = size
        except Exception:
            raise NameError("size must be an integer")
        else:
            if (size <= 0):
                raise NameError("size must be >= 0")
