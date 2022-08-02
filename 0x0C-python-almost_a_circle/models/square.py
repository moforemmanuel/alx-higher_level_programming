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
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """
        size getter method
        Returns: sizeof instance side

        """
        return self.__size

    @size.setter
    def size(self, size: int):
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


if __name__ == '__main__':
    s = Square(2)
    # s.update(id=4302)
    # s.update(size=-1)
    print(s)
