import unittest
from Zadacha11 import SQUARE
from Zadacha11 import MAX_SQUARE


class TestSorting(unittest.TestCase):
    def test_1(self):
        arr = [2, 5, 1, 2, 3, 4, 7, 7, 6]
        res = MAX_SQUARE(arr)
        expected = 10
        self.assertFalse(not res)
        self.assertEqual(expected, res)

    def test_2(self):
        arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
        res = MAX_SQUARE(arr)
        expected = 0
        self.assertFalse(not res)
        self.assertEqual(expected, res)

    def test_3(self):
        arr = [5]
        res = MAX_SQUARE(arr)
        expected = 0
        self.assertFalse(not res)
        self.assertEqual(expected, res)

    def test_4(self):
        arr = []
        res = MAX_SQUARE(arr)
        expected = 0
        self.assertFalse(not res)
        self.assertEqual(expected, res)
