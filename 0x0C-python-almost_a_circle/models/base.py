#!/usr/bin/python3
'''Module for Base class.'''
from json import dumps, loads


class Base:
    '''This class will be the “base” of all other classes in this project'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''Constructor.'''

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)
