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

if __name__ == '__main__':
    unittest.main()