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
            Base.__nb_objects += 1
            self.id = Base.__nb_objects


if __name__ == "__main__":
    b = Base()
    print(b.id)
    b2 = Base()
    print(b2.id)
    b3 = Base()
    print(b3.id)
    b4 = Base()
    print(b4.id)
