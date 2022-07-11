#!/usr/bin/python3
"""This is a basic test"""

import unittest


class TestString(unittest.TestCase):
    """This is a test case for strings"""

    def test_alnum(self):
        """This is a test for alnum chars"""
        self.assertEqual('hello'.isalnum(), True)


if __name__ == "__main__":
    unittest.main()
