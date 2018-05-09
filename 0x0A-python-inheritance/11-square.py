#!/usr/bin/python3

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ square class"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ area """
        return super().area()

    def __str__(self):
        return '[Square] {:d}/{:d}'.format(self.__size, self.__size)
