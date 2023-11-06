#!/usr/bin/python3
"""
    a class Square that inherits from Rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """define the class"""
    def __init__(self, size):
        """initialize the own property of size"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """get the string that reps the object, rectag"""
        return '[Square] {}/{}'.format(self.__size, self.__size)

    def area(self):
        """this module creates an area"""
        return self.__size ** 2
