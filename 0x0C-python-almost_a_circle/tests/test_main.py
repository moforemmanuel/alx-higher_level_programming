import unittest


class TestString(unittest.TestCase):
    def test_alnum(self):
        self.assertEqual('hello'.isalnum(), True)


if __name__ == "__main__":
    unittest.main()
