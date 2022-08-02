#!/usr/bin/python3
"""
This module implements a square object
"""

# pylint: disable=redefined-builtin

from .rectangle import Rectangle


class Square(Rectangle):
    """
    Class implementation of a square
    """
    def __init__(self, size: int, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """
        size getter method
        Returns: sizeof instance side

        """
        return self.size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size <= 0:
            raise ValueError("size must be > 0")
        self.size = size
        self.height = self.width = size

    def __str__(self):
        """
        overloading string repr
        Returns: instance repr
        """
        return f'[{self.__class__.__name__}] ({self.id})' \
               f' {self.x}/{self.y} - {self.size}'


if __name__ == '__main__':
    s = Square(2, 2, 2, 2)
    s.update(id=4302)
    s.update(size=-1)
    print(s)
