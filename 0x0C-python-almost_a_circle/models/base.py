#!/usr/bin/python3
'''Module for Base class.'''
from json import dumps, loads
import os
import csv


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

    @classmethod
    def save_to_file(cls, list_objs):
        """Save JSON string representation of list_objs to a file."""
        filename = cls.__name__ + ".json"

        if list_objs is None:
            list_dicts = []
        else:
            list_dicts = [obj.to_dictionary() for obj in list_objs]

        json_str = cls.to_json_string(list_dicts)

        with open(filename, "w") as f:
            f.write(json_str)

    def from_json_string(json_string):
        """returns the list of the JSON string representation"""
        if json_string is None or not json_string:
            return []
        else:
            return loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = None

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Loads list of instances from <Class name>.json file"""
        filename = f"{cls.__name__}.json"
        if not os.path.exists(filename):
            return []

        with open(filename, "r") as f:
            json_str = f.read()
            list_dicts = cls.from_json_string(json_str)
            return [cls.create(**d) for d in list_dicts]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = f"{cls.__name__}.csv"
        if list_objs is None:
            list_objs = []

        with open(filename, "w", newline='') as csvfile:
            writer = csv.writer(csvfile)

            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    row = [obj.id, obj.width, obj.height, obj.x, obj.y]
                elif cls.__name__ == "Square":
                    row = [obj.id, obj.size, obj.x, obj.y]
                else:
                    row = []
                writer.writerow(row)

    @classmethod
    def load_from_file_csv(cls):
        filename = f"{cls.__name__}.csv"
        if not os.path.exists(filename):
            return []

        with open(filename, "r", newline='') as csvfile:
            reader = csv.reader(csvfile)
            instances = []

            for row in reader:
                if cls.__name__ == "Rectangle":
                    id_, width, height, x, y = map(int, row)
                    dict_obj = {
                        "id": id_,
                        "width": width,
                        "height": height,
                        "x": x,
                        "y": y
                    }
                elif cls.__name__ == "Square":
                    id_, size, x, y = map(int, row)
                    dict_obj = {
                        "id": id_,
                        "size": size,
                        "x": x,
                        "y": y
                    }
                else:
                    dict_obj = {}

                instance = cls.create(**dict_obj)
                instances.append(instance)

        return instances
