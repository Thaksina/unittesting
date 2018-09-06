import unittest
from listunit import count_unique


class Testing(unittest.TestCase):

    def test_borderline_case(self):
        list = ["a"]
        self.assertEqual(1, count_unique(list))

    def test_typical_cases(self):
        list = ["d","f","i","s"]
        self.assertEqual(3, count_unique(list))

    def test_impossible_cases(self):
        list = [None]
        self.assertEqual(1, count_unique(list))

    def test_extreme_cases(self):
        list = ["a"]
        self.assertEqual(1, count_unique(list))
