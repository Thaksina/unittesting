import unittest
from binary_search import binarysearch

class TestingBinarySearch(unittest.TestCase):

    def test_findIndexof(self):
        self.assertEqual(binarysearch(['a','b','c'],'c'), 2)


    def test_NoneElemant(self):
        self.assertEqual(binarysearch(['a','b','c'],None), -1)

    def test_NotFindElement(self):
        self.assertEqual(binarysearch(['a','s','g'],'w'), -1)
