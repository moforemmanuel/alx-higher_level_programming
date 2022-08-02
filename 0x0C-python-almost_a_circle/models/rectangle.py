#!/usr/bin/python3
"""First Rectangle"""


# pylint: disable=too-many-arguments, unused-argument
# pylint: disable=invalid-name, redefined-builtin
# pylint: disable=relative-beyond-top-level
# pylint: disable=too-many-instance-attributes
# pylint: disable=unbalanced-tuple-unpacking
# pylint: disable=attribute-defined-outside-init
# pylint: disable=access-member-before-definition


from .base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def size(self):
        """getter for size"""
        return self.size

    @size.setter
    def size(self, width):
        """setter for width"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, height):
        """setter for height"""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """getter for x"""
        return self.__x

    @x.setter
    def x(self, x):
        """setter for x"""
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """getter for y"""
        return self.__y

    @y.setter
    def y(self, y):
        """setter for y"""
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """
        this is the area method which returns width * height
        """
        return self.height * self.width

    def display(self):
        """
        display instance graphically
        """
        s1 = ' ' * self.x
        s2 = '#' * self.width
        s = s1 + s2
        ts = '\n' * self.y
        i = self.height

        print(ts, end='')
        while i > 0:
            print(s)
            i -= 1

    def __str__(self):
        """
        Str repr
        """
        return f'[{self.__class__.__name__}] ({self.id})' \
               f' {self.__x}/{self.__y} - {self.__width}/{self.__height}'

    def update(self, *args, **kwargs):
        """

        Args:
            *args: integers to update args
            **kwargs: named args to update instance

        Returns:

        """
        values = (self.id, self.width, self.height, self.x, self.y)
        if args:
            self.id, self.width, self.height, self.x, self.y =\
                args + values[len(args):]

        elif kwargs:
            for (name, value) in kwargs.items():
                setattr(self, name, value)


if __name__ == "__main__":
    r = Rectangle(4, 2, 2, 2)
    r.update(id=20)
    print(r)
