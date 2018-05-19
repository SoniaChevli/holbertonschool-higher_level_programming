#!/usr/bin/python3


class Base:
    """ Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        initalize base attributes

        Args:
        id (int): id number for base

        Returns:
        None
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
