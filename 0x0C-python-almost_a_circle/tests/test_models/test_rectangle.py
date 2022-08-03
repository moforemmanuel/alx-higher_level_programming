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
        rect1 = Rectangle()
        rect2 = Rectangle()
        self.assertEqual(rect1.id, 1)
        self.assertEqual(rect2.id, 2)