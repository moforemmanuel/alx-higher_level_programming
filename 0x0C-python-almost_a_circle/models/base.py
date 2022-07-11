#!/usr/bin/python3
"""models"""
# pylint: disable=invalid-name, redefined-builtin, too-few-public-methods


class Base:
    """base model"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        if id is not None:
            self.id = id
        else:
            self.__nb_objects += 1
            self.id = self.__nb_objects
