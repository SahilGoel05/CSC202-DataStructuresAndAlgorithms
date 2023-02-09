import unittest
from stack_array import Stack
        
class TestLab2(unittest.TestCase):

    def test_init(self) -> None:
        stack = Stack(5)
        self.assertEqual(stack.items, [None]*5)
        self.assertEqual(stack.capacity, 5)

        stack = Stack(5, [1, 2])
        self.assertEqual(stack.items[0:2], [1, 2])
        self.assertEqual(stack.capacity, 5)

        with self.assertRaises(IndexError):
            Stack(5, [1, 2, 3, 4, 5, 6])

    def test_eq(self) -> None:
        stack1 = Stack(5)
        stack2 = Stack(5)
        stack3 = Stack(10)
        stack4 = Stack(5,[1, 2])
        self.assertEqual(stack1, stack2)
        self.assertNotEqual(stack1, stack3)
        self.assertNotEqual(stack1, stack4)
        self.assertFalse(stack1.__eq__(None))

    def test_repr(self) -> None:
        stack = Stack(5, [1, 2])
        self.assertEqual(stack.__repr__(), "Stack(5, [1, 2])")

    def test_push_1(self) -> None:
        startStack = Stack(10)
        startStack.push(1)
        startStack.push(2)
        startStack.push(3)
        startStack.push(4)
        startStack.push("Why")
        finalStack = Stack(10, [1, 2, 3, 4, "Why"])
        self.assertEqual(startStack, finalStack)

    def test_push_2(self) -> None:
        startStack = Stack(3)
        startStack.push(1)
        startStack.push(2)
        startStack.push(3)
        with self.assertRaises(IndexError):
            startStack.push("Nay")

    def test_pop_1(self) -> None:
        startStack = Stack(5, [1, 2, 3, 4, 5])
        startStack.pop()
        startStack.pop()
        startStack.pop()
        finalStack = Stack(5, [1, 2])
        self.assertEqual(startStack, finalStack)

    def test_pop_2(self) -> None:
        startStack = Stack(2, [1, 2])
        startStack.pop()
        startStack.pop()
        with self.assertRaises(IndexError):
            startStack.pop()

    def test_peek_1(self) -> None:
        stack = Stack(5, [1, 2, 3])
        self.assertEqual(stack.peek(), 3)
        stack.pop()
        self.assertEqual(stack.peek(), 2)
        stack.push("HI!!!!")
        self.assertEqual(stack.peek(), "HI!!!!")

    def test_peek_2(self) -> None:
        stack = Stack(5, [1, 2])
        self.assertEqual(stack.peek(), 2)
        stack.pop()
        stack.pop()
        with self.assertRaises(IndexError):
            stack.peek()

    def test_size(self) -> None:
        stack = Stack(999999, [1, 2, "hi", "there", 5])
        self.assertEqual(stack.size(), 5)
        stack = Stack(100)
        self.assertEqual(stack.size(), 0)
        stack = Stack(0)
        self.assertEqual(stack.size(), 0)
        stack = Stack(3, ["1", "2", "3"])
        self.assertEqual(stack.size(), 3)

    def test_is_full(self) -> None:
        stack = Stack(999999, [1, 2, "hi", "there", 5])
        self.assertFalse(stack.is_full())
        stack = Stack(3, ["1", "2", "3"])
        self.assertTrue(stack.is_full())

    def test_is_empty(self) -> None:
        stack = Stack(999999, [1, 2, "hi", "there", 5])
        self.assertFalse(stack.is_empty())
        stack = Stack(3, ["1", "2", "3"])
        self.assertFalse(stack.is_empty())
        stack = Stack(1000)
        self.assertTrue(stack.is_empty())
        stack = Stack(100, [])
        self.assertTrue(stack.is_empty())

# WRITE TESTS FOR STACK OPERATIONS - PUSH, POP, PEEK, etc.

if __name__ == '__main__': 
    unittest.main()
