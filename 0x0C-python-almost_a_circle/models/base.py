#!/usr/bin/python3
import json
import ast

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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ 
        returns the JSON string rep of list__dictionaries
        """
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes JSON string rep of list_objs
        """
        with open('{}.json'.format(cls.__name__), 'w') as outputfile:
            l = []
            for i in list_objs:
                l.append(i.to_dictionary())
            outputfile.write(Base.to_json_string(l))

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation
        Args:
        json_string(str): string rep of list of dictionaries
        """
        if json_string == None or json_string == '':
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        gives an instance with all attributes set

        Args:
        **dictionary (double pointer): points to a dictionary

        Return:
        an instance with all attributes set

        """
        
        from models.rectangle import Rectangle
        from models.square import Square

        if cls.__name__ == 'Square':
            j = Square(1)
            j.update(**dictionary)
            return j
        if cls.__name__ == 'Rectangle':
            j = Rectangle(1, 1)
            j.update(**dictionary)
            return j

    @classmethod
    def load_from_file(cls):
        """
        gives a list of the instances
        Args:
        cls: current class using this method

        Return:
        a list of instances. Otherwise an empty list
        """
        with open('{}.json'.format(cls.__name__), 'r') as f:
            new = []
            fr = f.read()
            j = cls.from_json_string(fr)
            for i in j:
                k = cls.create(**i)
                new.append(k)
            return new


