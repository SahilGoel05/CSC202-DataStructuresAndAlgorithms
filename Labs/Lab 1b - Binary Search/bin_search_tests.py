import unittest
from bin_search import *
from typing import List

class TestLab1b(unittest.TestCase):

    def test_bin_search_iter_01(self) -> None:
        tlist: List = [5, 9, 18, 23, 55, 72]
        self.assertEqual(bin_search_iter(tlist, 5), 0)

    def test_bin_search_iter_02(self) -> None:
        tlist = None
        with self.assertRaises(ValueError):  # uses context manager for checking exception
            bin_search_iter(tlist, 5)

    def test_bin_search_iter_03(self) -> None:
        tlist: List = [5, 9, 18, 23, 55, 72]
        self.assertEqual(bin_search_iter(tlist, 54), None)

    def test_bin_search_iter_04(self) -> None:
        tlist: List = [5, 9, 18, 23, 55, 72, 82, 99, 103, 583, 1035, 1923, 2000]
        self.assertEqual(bin_search_iter(tlist, 1035), 10)

    def test_bin_search_iter_05(self) -> None:
        tlist: List = [5, 9, 18, 23, 55, 72, 82, 99, 103, 583, 1035, 1923, 2000]
        self.assertEqual(bin_search_iter(tlist, 82), 6)

    def test_bin_search_iter_06(self) -> None:
        tlist: List = []
        self.assertEqual(bin_search_iter(tlist, 12), None)


    def test_bin_search_rec_01(self) -> None:
        tlist: List = [5, 9, 18, 23, 55, 72]
        self.assertEqual(bin_search_rec(tlist, 9), 1)

    def test_bin_search_rec_02(self) -> None:
        tlist = None
        with self.assertRaises(ValueError):  # uses context manager for checking exception
            bin_search_rec(tlist, 5)

    def test_bin_search_rec_03(self) -> None:
        tlist: List = [5, 9, 18, 23, 55, 72]
        self.assertEqual(bin_search_rec(tlist, 54), None)

    def test_bin_search_rec_04(self) -> None:
        tlist: List = [5, 9, 18, 23, 55, 72, 82, 99, 103, 583, 1035, 1923, 2000]
        self.assertEqual(bin_search_rec(tlist, 1035), 10)

    def test_bin_search_rec_05(self) -> None:
        tlist: List = [5, 9, 18, 23, 55, 72, 82, 99, 103, 583, 1035, 1923, 2000]
        self.assertEqual(bin_search_rec(tlist, 82), 6)

    def test_bin_search_rec_06(self) -> None:
        tlist: List = []
        self.assertEqual(bin_search_rec(tlist, 12), None)

if __name__ == "__main__":
        unittest.main()
