import unittest
from Zadacha6 import RADIX_SORT


class TestSorting(unittest.TestCase):
    def test_trivial(self):
        arr1 = [1, 333, 22]
        arr2 = []
        res = RADIX_SORT(arr1, arr2)
        expected = [1, 22, 333]
        self.assertFalse(not res)
        self.assertEqual(expected, res)

    def test_empty(self):
        arr1 = []
        arr2 = []
        res = RADIX_SORT(arr1, arr2)
        expected = []
        self.assertEqual(expected, res)

    def test_1(self):
        arr1 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
                2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 8]
        arr2 = []
        res = RADIX_SORT(arr1, arr2)
        expected = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
                    2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 8]
        self.assertEqual(expected, res)

    def test_2(self):
        arr1 = []
        arr2 = [-111, -222, -333, -123, -321, -231, -213, -132, -312, -10, -5]
        res = RADIX_SORT(arr1, arr2)
        expected = [-333, -321, -312, -231, -222, -213, -132, -123, -111, -10, -5]
        self.assertEqual(res, expected)
