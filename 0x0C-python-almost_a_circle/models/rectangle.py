#!/usr/bin/python3
"""First Rectangle"""

# pylint: disable=invalid-name, redefined-builtin, too-many-arguments, unused-argument
from .base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def get_width(self):
        """getter for width"""
        return self.__width

    def set_width(self, width):
        """setter for width"""
        self.__width = width

    def get_height(self, width):
        """getter for height"""
        return self.__height

    def set_height(self, height):
        """setter for height"""
        self.__height = height

    def get_x(self):
        """getter for x"""
        return self.__x

    def set_x(self, x):
        """setter for x"""
        self.__x = x

    def get_y(self, y):
        """getter for y"""
        return self.__y

    def set_y(self, y):
        """setter for y"""
        self.__y = y
