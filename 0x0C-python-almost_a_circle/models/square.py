#!/usr/bin/python3
"""
This module implements a square object
"""

# pylint: disable=redefined-builtin
# pylint: disable=unbalanced-tuple-unpacking

from .rectangle import Rectangle


class Square(Rectangle):
    """
    Class implementation of a square
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.__size = size

    @property
    def size(self):
        """
        size getter method
        Returns: sizeof instance side

        """
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
        self.__size = size
        self.width = self.height = size

    def __str__(self):
        """
        overloading string repr
        Returns: instance repr
        """
        return f'[{self.__class__.__name__}] ({self.id})' \
               f' {self.x}/{self.y} - {self.__size}'

    def update(self, *args, **kwargs):
        """
        Args:
            *args: integers to update args
            **kwargs: named args to update instance

        Returns:

        """
        values = (self.id, self.size, self.x, self.y)
        if args:
            self.id, self.size, self.x, self.y =\
                args + values[len(args):]

        elif kwargs:
            for (name, value) in kwargs.items():
                setattr(self, name, value)


if __name__ == '__main__':
    s = Square(-1)
    # s.update(id=4302)
    # s.update(size=-1)
    print(s)
