from __future__ import annotations
from queue_array import Queue
from typing import Optional, Any, Tuple, List


class TreeNode:
    def __init__(self, key: Any, data: Any, left: Optional[TreeNode] = None, right: Optional[TreeNode] = None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right

    def __eq__(self, other: object) -> bool:
        if isinstance(other, TreeNode):
            return (self.key == other.key
                    and self.data == other.data
                    and self.left == other.left
                    and self.right == other.right)
        else:
            return False

    def __repr__(self) -> str:
        return ("TreeNode({!r}, {!r}, {!r}, {!r})".format(self.key, self.data, self.left, self.right))


class BinarySearchTree:
    def __init__(self, root_node: Optional[TreeNode] = None):  # Returns empty BST
        self.root: Optional[TreeNode] = root_node

    # returns True if tree is empty, else False
    def is_empty(self) -> bool:
        if self.root is None:
            return True
        return False

    # returns True if key is in a node of the tree, else False
    def search(self, key: Any) -> bool:
        if self.is_empty():
            return False
        current_node = self.root
        while current_node.left or current_node.right:
            if key == current_node.key:
                return True
            elif key < current_node.key:
                if current_node.left:
                    current_node = current_node.left
                else:
                    return False
            elif key > current_node.key:
                if current_node.right:
                    current_node = current_node.right
                else:
                    return False
        if key == current_node.key:
            return True
        return False

    # Inserts new node w/ key and data
    # If an item with the given key is already in the BST,
    # the data in the tree will be replaced with the new data
    # Example creation of node: temp = TreeNode(key, data)
    # On insert, can assume key not already in BST
    def insert(self, key: Any, data: Any = None) -> None:
        if self.is_empty():
            self.root = TreeNode(key, data)
        else:
            inserted = False
            current_node = self.root
            while (current_node.left or current_node.right) and not inserted:
                if key == current_node.key:
                    current_node.data = data
                    inserted = True
                elif key < current_node.key:
                    if current_node.left:
                        current_node = current_node.left
                    else:
                        current_node.left = TreeNode(key, data)
                        current_node = current_node.left
                        inserted = True
                elif key > current_node.key:
                    if current_node.right:
                        current_node = current_node.right
                    else:
                        current_node.right = TreeNode(key, data)
                        current_node = current_node.right
                        inserted = True
            if not inserted:
                if key == current_node.key:
                    current_node.data = data
                elif key < current_node.key:
                    current_node.left = TreeNode(key, data)
                elif key > current_node.key:
                    current_node.right = TreeNode(key, data)

    # returns tuple with min key and associated data in the BST
    # returns None if the tree is empty
    def find_min(self) -> Optional[Tuple[Any, Any]]:
        if self.is_empty():
            return None
        current_node = self.root
        while current_node.left:
            current_node = current_node.left
        return tuple((current_node.key, current_node.data))

    # returns tuple with max key and associated data in the BST
    # returns None if the tree is empty
    def find_max(self) -> Optional[Tuple[Any, Any]]:
        if self.is_empty():
            return None
        current_node = self.root
        while current_node.right:
            current_node = current_node.right
        return tuple((current_node.key, current_node.data))

    # returns the height of the tree
    # if tree is empty, return None
    def tree_height(self) -> Optional[int]:
        if self.is_empty():
            return None
        return self.tree_height_helper(self.root) - 1

    def tree_height_helper(self, current_node: Optional[TreeNode]) -> Optional[int]:
        if current_node is None:
            return 0

        tryLeft = self.tree_height_helper(current_node.left)
        tryRight = self.tree_height_helper(current_node.right)

        return max(tryLeft, tryRight) + 1


    # returns Python list of BST keys representing inorder traversal of BST
    def inorder_list(self) -> List:
        return self.inorder_helper(self.root)

    def inorder_helper(self, current_node: Optional[TreeNode]) -> List:
        ret: List = []
        if current_node:
            ret = self.inorder_helper(current_node.left)
            ret.append(current_node.key)
            ret = ret + self.inorder_helper(current_node.right)
        return ret


    # returns Python list of BST keys representing preorder traversal of BST
    def preorder_list(self) -> List:
        return self.preorder_helper(self.root)

    def preorder_helper(self, current_node: Optional[TreeNode]) -> List:
        ret: List = []
        if current_node:
            ret.append(current_node.key)
            ret = ret + self.preorder_helper(current_node.left)
            ret = ret + self.preorder_helper(current_node.right)
        return ret

    # returns Python list of BST keys representing level-order traversal of BST
    # You MUST use your queue_array data structure from lab 3 to implement this method
    def level_order_list(self) -> List:
        q = Queue(25000)  # Don't change this!
        ret: List = []

        if self.is_empty():
            return ret
        q.enqueue(self.root)

        while not q.is_empty():
            q_len = q.size()
            level_vals: List = []

            while q_len > 0:
                current_node = q.dequeue()
                level_vals.append(current_node.key)
                q_len -= 1
                if current_node.left:
                    q.enqueue(current_node.left)
                if current_node.right:
                    q.enqueue(current_node.right)

            for i in range(len(level_vals)):
                ret.append(level_vals[i])

        return ret

