#!/usr/bin/python3

"""Base Test"""
import unittest
from ..models.base import Base

base = Base()

class BaseTest(unittest.TestCase):
    """Test for base id"""

    def test_id(self):
        """test case"""
        self.assertNotEqual(base.id, None)
