#!/usr/bin/python3
"""Unittests for base
"""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    rect test model
    """
    def test_initialization(self):
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.id, Rectangle._Base__nb_objects)
        r2 = Rectangle(1, 2, 3)
        self.assertEqual(r2.id, Rectangle._Base__nb_objects)
        r3 = Rectangle(1, 2, 3, 4)
        self.assertEqual(r3.id, Rectangle._Base__nb_objects)
        r4 = Rectangle("1", 2)
        self.assertRaises(TypeError)
        self.assertNotEqual(Rectangle("1", 2), Rectangle._Base__nb_objects)
        # self.assertRaises(Rectangle(1, 2, "3"), TypeError)
        # self.assertRaises(Rectangle(1, 2, 3, "4"), TypeError)
        # self.assertEqual(Rectangle(1, 2, 3, 4, 4), Rectangle._Base__nb_objects)
        self.assertRaises((ValueError, TypeError))

    def test_of_area(self):
        rect = Rectangle(2, 3)
        self.assertEqual(rect.area(), rect.width * rect.height)

    def test_of__str__(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(print(r), '[Rectangle] (4) 4/5 - 1/2')

    def test_of_display(self):
        self.assertNotEqual(Rectangle(1, 2), '')

    def test_of_to_dictionary(self):
        self.assertNotEqual(Rectangle(1, 2), None)

    def test_of_update(self):
        r = Rectangle(1, 2)
        r.update(id=4)
        self.assertEqual(r.id, 4)


if __name__ == '__main__':
    unittest.main()