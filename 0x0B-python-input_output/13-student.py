#!/usr/bin/python3


class Student:
    """ class defined as student"""
    def __init__(self, first_name, last_name, age):
        """instantiation of square class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ gives all the attibutes"""
        at = {}
        if isinstance(attrs, list):
            for key in attrs:
                if key in self.__dict__:
                    at[key] = self.__dict__[key]
            return at
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """ replaces all attributes of the student instance"""
        self.__dict__ = json
