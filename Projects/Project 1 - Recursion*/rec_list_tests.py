import unittest
from  rec_list import *

# Starter test cases - write more!!

class TestRecList(unittest.TestCase):

    def test_first1(self) -> None:
        strlist = Node("xyz", Node("Abc", Node("49ers", None)))
        self.assertEqual(first_string(strlist),"49ers")

    def test_first2(self) -> None:
        strlist = Node("Yellow", Node("abc", Node("7.25", Node("lime", Node("42", Node("Ethan", None))))))
        self.assertEqual(first_string(strlist),"42")

    def test_first3(self) -> None:
        strlist = Node(None, None)
        self.assertEqual(first_string(strlist), None)

    def test_first4(self) -> None:
        strlist = None
        with self.assertRaises(ValueError):  # uses context manager for checking exception
            first_string(strlist)

    def test_split1(self) -> None:
        strlist = Node("xyz", Node("Abc", Node("49ers", None)))
        self.assertEqual(split_list(strlist),(Node('Abc', None), Node('xyz', None), Node('49ers', None)))

    def test_split2(self) -> None:
        strlist = Node("Yellow", Node("abc", Node("$7.25", Node("lime", Node("42", Node("Ethan", None))))))
        self.assertEqual(split_list(strlist),(Node('abc', Node('Ethan', None)), Node('Yellow', Node('lime', None)), Node('$7.25', Node('42', None))))

    def test_split3(self) -> None:
        strlist = Node("Ethan", Node("abc", Node("$7.25", Node("lime", Node("42", Node("Yellow", None))))))
        self.assertEqual(split_list(strlist),(Node('Ethan', Node('abc', None)), Node('lime', Node('Yellow', None)), Node('$7.25', Node('42', None))))

    def test_split4(self) -> None:
        strlist = Node(None, None)
        self.assertEqual(split_list(strlist), None)

    def test_split5(self) -> None:
        strlist = None
        with self.assertRaises(ValueError):  # uses context manager for checking exception
            split_list(strlist)

if __name__ == "__main__":
        unittest.main()
