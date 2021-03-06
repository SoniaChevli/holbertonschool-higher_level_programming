#!/usr/bin/python3
''' module for rectangle class '''
from models.base import Base


class Rectangle(Base):
    """ Rectangle class that inherites from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initalize Rectangle attributes

        Args:
        width (int): width of rectangle
        height (int): height of rectangle
        x (int):
        y (int):
        id (int): id of rectangle

        Return:
        Nothing
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        width setter

        Args:
        value (int): value to set to width
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """ height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Height setter

        Args:
        value (int): value to set to height

        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """ x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """
        x setter

        Args:
        value (int): value is set to x
        """
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """ y getter """
        return self.__y

    @y.setter
    def y(self, value):
        """
        y setter

        Args:
        value (int): value is set to y

        """
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """ area of rectangle"""
        return self.__height * self.__width

    def display(self):
        """ prints rectangle """
        for i in range(self.__y):
            print()
        for h in range(self.__height):
            for j in range(self.__x):
                print(' ', end='')
            for w in range(self.__width):
                print('#', end='')
            print()

    def __str__(self):
        """overloads the str method"""
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(self.id,
                                                       self.__x, self.__y,
                                                       self.__width,
                                                       self.__height)

    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute"""

        argnum = len(args)
        if argnum != 0:
            if argnum >= 1:
                self.id = args[0]
            if argnum >= 2:
                self.__width = args[1]
            if argnum >= 3:
                self.__height = args[2]
            if argnum >= 4:
                self.__x = args[3]
            if argnum >= 5:
                self.__y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ gives the dictionary representation of Rectangle"""
        final = {}
        for key, value in self.__dict__.items():
            if key == 'id':
                final['id'] = value
            if key == '_Rectangle__width':
                final['width'] = value
            if key == '_Rectangle__height':
                final['height'] = value
            if key == '_Rectangle__x':
                final['x'] = value
            if key == '_Rectangle__y':
                final['y'] = value
        return final
