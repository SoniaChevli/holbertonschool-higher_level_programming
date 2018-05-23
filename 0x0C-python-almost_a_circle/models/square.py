#!/usr/bin/python3
'''
module for square
'''
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square Class """
    def __init__(self, size, x=0, y=0, id=None):
        """
        initation of square class

        Args:
        size (int): size of square
        x (int): x number of spaces
        y (int): y number of newlines before square
        id (int): number identifier for square

        Return:
        Nothing
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ overload str method """
        return '[Square] ({:d}) {:d}/{:d} - {:d}'.format(self.id,
                                                         self.x,
                                                         self.y,
                                                         self.width)

    @property
    def size(self):
        """ size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """ size setter"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ update the attributes
        Args:
        *args: list of arguments to change attributes to
        **kwargs: dicyionary to keyword arguments

        Return:
        Nothing
        """
        argnum = len(args)
        if argnum != 0:
            if argnum >= 1:
                self.id = args[0]
            if argnum >= 2:
                self.size = args[1]
            if argnum >= 3:
                self.x = args[2]
            if argnum >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ gives the dictionary representation of Rectangle"""
        final = {}
        attrib = ['size', 'x', 'y', 'id']
        for i in attrib:
            final[i] = getattr(self, i)
        return final
