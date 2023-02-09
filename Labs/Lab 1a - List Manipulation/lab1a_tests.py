# CPE 202 Lab 1a - List Manipulation Test Cases

import unittest
from lab1a import *

# A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_01(self) -> None:
        tlist = [1, 2, 3]
        self.assertEqual(max_list_iter(tlist), 3)

    """test  if the the max_list_iter function will retrieve the maximum
    number from a list"""

    def test_max_list_02(self) -> None:
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

    """test  if the the max_list_iter function will raise ValueError
    when a list is not passed in"""

    def test_max_list_03(self) -> None:
        tlist: List = []
        self.assertEqual(max_list_iter(tlist), None)

    """test  if the the max_list_iter function will return None if an empty list
    is passed in"""

    def test_reverse_01(self) -> None:
        intlist = [1,2,3]
        revlist = reverse_list(intlist)
        self.assertEqual(revlist,[3,2,1])
        self.assertEqual(intlist,[1,2,3])

    """test  if the the reverse_list function will reverse the list that
    is passed in"""

    def test_reverse_02(self) -> None:
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_list(tlist)

    """test  if the the reverse_list function will raise ValueError when a
    list is not passed in"""

    def test_reverse_mutate_01(self) -> None:
        intlist = [1,2,3]
        reverse_list_mutate(intlist)
        self.assertEqual(intlist,[3,2,1])

    """test if the reverse_list_mutate function will reverse the input list
    that's passed in"""

    def test_reverse_mutate_02(self) -> None:
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_list_mutate(tlist)

    """test if the reverse_list_mutate function will raise ValueError when a
    list is not passed in"""

if __name__ == "__main__":
        unittest.main()
