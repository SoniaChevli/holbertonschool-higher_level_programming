#!/usr/bin/python3


class Rectangle:

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * self.__width + 2 * self.__height

    def __str__(self):
        hashtangle = ''
        if self.__height == 0 or self.__width == 0:
            return hashtangle
        for i in range(self.__height):
            hashtangle += "#" * self.__width
            if i != self.__height - 1:
                hashtangle += '\n'
        return hashtangle

    def __repr__(self):
        return "Rectangle(" + str(self.__height) + ", " + str(self.__width) +\
            ")"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
