#!/usr/bin/python3
"""
Add integers module
two numbers
return result
"""


def add_integer(a, b=98):
    """ adds two integers
    args: a and b
    returns: addition of both """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)


if __name__ == '__main__':
    import doctest
    doctest.testfile("./tests/0-add_integer.txt")
