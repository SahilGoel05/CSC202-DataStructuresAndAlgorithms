import unittest
from stack_nodelist import *
        
class TestLab2(unittest.TestCase):

    def test_node_init(self) -> None:
        node1 = Node(1, None)
        self.assertEqual(node1.value, 1)
        self.assertEqual(node1.rest, None)

        node2 = Node(2, node1)
        self.assertEqual(node2.value, 2)
        self.assertEqual(node2.rest, node1)

    def test_node_eq(self) -> None:
        node1a = Node(1, None)
        node1b = Node(1, None)
        node2a = Node(2, node1a)
        node2b = Node(2, node1b)

        self.assertEqual(node1a, node1b)
        self.assertNotEqual(node1a, node2a)
        self.assertEqual(node2a, node2b)
        node1a = Node(3, None)
        self.assertNotEqual(node1a, node1b)

        self.assertFalse(node1a.__eq__(None))

    def test_node_repr(self) -> None:
        node = Node(2, Node(1, None))
        self.assertEqual(node.__repr__(), "Node(2, Node(1, None))")

    def test_stack_init(self) -> None:
        stack = Stack()
        self.assertEqual(stack.top, None)

        init_stack = Node(2, Node(1, None))
        stack = Stack(init_stack)
        self.assertEqual(stack.top, init_stack)

    def test_stack_eq(self) -> None:
        stack1 = Stack()
        stack2 = Stack()
        init_stack = Node(2, Node(1, None))
        stack4 = Stack(init_stack)
        self.assertEqual(stack1, stack2)
        self.assertNotEqual(stack1, stack4)
        self.assertFalse(stack1.__eq__(None))

    def test_stack_repr(self) -> None:
        init_stack = Node(2, Node(1, None))
        stack = Stack(init_stack)
        self.assertEqual(stack.__repr__(), "Stack(Node(2, Node(1, None)))")

    def test_stack_is_empty(self) -> None:
        stack1 = Stack()
        self.assertTrue(stack1.is_empty())
        stack1.push("not")
        stack1.push("empty")
        stack1.push("anymore")
        self.assertFalse(stack1.is_empty())

    def test_stack_push(self) -> None:
        startStack = Stack()
        startStack.push("1")
        startStack.push("2")
        startStack.push("3")
        init_stack = Node("3", Node("2", Node("1", None)))
        finalStack = Stack(init_stack)
        self.assertEqual(startStack, finalStack)

    def test_stack_pop1(self) -> None:
        init_stack = Node("3", Node("2", Node("1", None)))
        startStack = Stack(init_stack)
        startStack.pop()
        startStack.pop()
        init_stack = Node("1", None)
        finalStack = Stack(init_stack)
        self.assertEqual(startStack, finalStack)

    def test_stack_pop2(self) -> None:
        init_stack = Node("1", None)
        startStack = Stack(init_stack)
        startStack.pop()
        with self.assertRaises(IndexError):
            startStack.pop()

    def test_stack_peek(self) -> None:
        startStack = Stack()
        with self.assertRaises(IndexError):
            startStack.peek()
        init_stack = Node("3", Node("2", Node("1", None)))
        startStack = Stack(init_stack)
        self.assertEqual(startStack.peek(), "3")

    def test_stack_size(self) -> None:
        startStack = Stack()
        self.assertEqual(startStack.size(), 0)
        init_stack = Node("3", Node("2", Node("1", None)))
        startStack = Stack(init_stack)
        self.assertEqual(startStack.size(), 3)
        self.assertNotEqual(startStack.size(), 2)

# WRITE TESTS FOR STACK OPERATIONS - PUSH, POP, PEEK, etc.

if __name__ == '__main__': 
    unittest.main()
