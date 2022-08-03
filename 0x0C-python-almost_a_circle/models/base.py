#!/usr/bin/python3
"""models"""
# pylint: disable=invalid-name, redefined-builtin, too-few-public-methods

import json


class Base:
    """base model"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        return '[]'

    @classmethod
    def save_to_file(cls, list_objs):
        fname = cls.__name__ + ".json"

        data = []
        if list_objs:
            for obj in list_objs:
                data.append(obj.to_dictionary())
        data_str = Base.to_json_string(data)

        with open(fname, 'w') as json_file:
            return json_file.write(data_str)

    @staticmethod
    def from_json_string(json_string):
        dict_obj = []
        if json_string:
            dict_obj = json.loads(json_string)
        return dict_obj

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == 'Rectangle':
            dummy = cls(2, 4)
        elif cls.__name__ == 'Square':
            dummy = cls(2)
        dummy.update(**dictionary)
