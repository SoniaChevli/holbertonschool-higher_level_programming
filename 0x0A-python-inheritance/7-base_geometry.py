#!/usr/bin/python3


class BaseGeometry:
    """ basegeometry class"""
    def __init__(self):
        """initation"""
    def area(self):
        """area"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError('{:s} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{:s} must be greater than 0'.format(name))

if __name__ == '__main__':
    import doctest
    doctest.testfile('./tests/7-base_geometry.txt')
