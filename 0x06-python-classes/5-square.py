#!/usr/bin/python3


class Square:
    """sqaure class"""
    def __init__(self, size=0):
        """instantiation"""
        self.__size = size

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for column in range(self.__size):
                for row in range(self.__size):
                    print("#", end='')
                print()

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
