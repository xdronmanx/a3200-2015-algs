import unittest
from Zadacha10 import PIF_COUTNER


class TestSorting(unittest.TestCase):
    def test_1(self):
        arr = [3, 4, 5, 3, 4, 5, 3, 4, 5, 3, 4, 5]
        res = PIF_COUTNER(arr)
        expected = 1
        self.assertEqual(expected, res)

    def test_2(self):
        arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
        res = PIF_COUTNER(arr)
        expected = 0
        self.assertEqual(expected, res)

    def test_3(self):
        arr = [5]
        res = PIF_COUTNER(arr)
        expected = 0
        self.assertEqual(expected, res)

    def test_4(self):
        arr = []
        res = PIF_COUTNER(arr)
        expected = 0
        self.assertEqual(expected, res)

    def test_5(self):
        arr = [3, 4, 5]
        res = PIF_COUTNER(arr)
        expected = 1
        self.assertEqual(expected, arr)
