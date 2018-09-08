import unittest
from listunit import count_unique
from listunit import binary_search

class Testing(unittest.TestCase):

    def test_borderline_case(self):
        list = ["a"]
        self.assertEqual(1, count_unique(list))

    def test_typical_cases(self):
        list = ["d","f","i"]
        self.assertEqual(3, count_unique(list))

    def test_impossible_cases(self):
        list = [None]
        self.assertEqual(0, count_unique(list))

    def test_extreme_cases(self):
        list = []
        for i in range (0,100000):
            list.append(1)
        self.assertEqual(1, count_unique(list))

    def test_findIndexof(self):
        self.assertEqual(binary_search(['a','b','c'],'c'), 2)


    def test_NoneElemant(self):
        self.assertEqual(binary_search(['a','b','c'],None), -1)

    def test_NotFindElement(self):
        self.assertEqual(binary_search(['a','s','g'],'w'), -1)
