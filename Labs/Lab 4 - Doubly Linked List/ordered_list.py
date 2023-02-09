from __future__ import annotations
from typing import Optional, Any, List

class Node:
    """Node for use with doubly-linked list"""
    def __init__(self, item: Any):
        self.item = item  # item held by Node
        self.next: Node = self  # reference to next Node, init to this Node
        self.prev: Node = self  # reference to previous Node, init to this Node

class OrderedList:
    """A doubly-linked ordered list of integers, 
    from lowest (head of list, sentinel.next) to highest (tail of list, sentinel.prev)"""
    def __init__(self) -> None:
        """Use only a sentinel Node. No other instance variables"""
        self.sentinel: Node = Node(None)    # Empty linked list, just sentinel Node
        self.sentinel.next = self.sentinel  # Initialize next to sentinel
        self.sentinel.prev = self.sentinel  # Initialize prev to sentinel

    def __eq__(self, other: object) -> bool:
        lists_equal = True
        if not isinstance(other, OrderedList):
            lists_equal = False
        else:
            s_cur = self.sentinel.next
            o_cur = other.sentinel.next
            while s_cur != self.sentinel and o_cur != other.sentinel:
                if s_cur.item != o_cur.item:
                    lists_equal = False
                s_cur = s_cur.next
                o_cur = o_cur.next
            if s_cur != self.sentinel or o_cur != other.sentinel:
                lists_equal = False
        return lists_equal

    def is_empty(self) -> bool:
        return self.sentinel.next == self.sentinel
        """Returns back True if OrderedList is empty"""

    def add(self, item: Any) -> None:
        temp = self.sentinel
        while temp.next != self.sentinel:
            if temp.next.item != item:
                if item > temp.next.item:
                    temp = temp.next
                else:
                    break
        temp2 = Node(item)
        temp2.prev = temp
        temp2.next = temp.next
        temp.next.prev = temp2
        temp.next = temp2
        """Adds an item to OrderedList, in the proper location based on ordering of items
        from lowest (at head of list) to highest (at tail of list)
        If item is already in list, do not add again (no duplicate items)"""

    def remove(self, item: Any) -> bool:
        if self.is_empty():
            return False
        temp = self.sentinel.next
        while temp != self.sentinel:
            if temp.item == item:
                temp.next.prev = temp.prev
                temp.prev.next = temp.next
                return True
            temp = temp.next
        return False
        """Removes an item from OrderedList. If item is removed (was in the list) returns True
        If item was not removed (was not in the list) returns False"""

    def index(self, item: Any) -> Optional[int]:
        temp = self.sentinel.next
        for x in range(self.size()):
            if temp.item == item:
                return x
            temp = temp.next
        return None
        """Returns index of an item in OrderedList (assuming head of list is index 0).
        If item is not in list, return None"""

    def pop(self, index: int) -> Any:
        if  index >= self.size() or index < 0:
            raise IndexError
        temp = self.sentinel.next
        for x in range(index):
            temp = temp.next
        final = temp.item
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        return final
        """Removes and returns item at index (assuming head of list is index 0).
        If index is negative or >= size of list, raises IndexError"""

    def search(self, item: Any) -> bool:
        return self.search_helper(item, self.sentinel.next)
    """Searches OrderedList for item, returns True if item is in list, False otherwise - USE RECURSION"""

    def search_helper(self, item, temp) -> bool:
        if temp == self.sentinel:
            return False
        if temp.item == item:
            return True
        return self.search_helper(item, temp.next)

    def python_list(self) -> List:
        if self.is_empty():
            return []
        return self.python_list_helper(self.sentinel.next)
    """Return a Python list representation of OrderedList, from head to tail
        For example, list with integers 1, 2, and 3 would return [1, 2, 3]"""

    def python_list_helper(self, temp):
        if temp.next == self.sentinel:
            return [temp.item]
        return [temp.item] + self.python_list_helper(temp.next)

    def python_list_reversed(self) -> List:
        if self.is_empty():
            return []
        return self.reverse_helper(self.sentinel.next)
    """Return a Python list representation of OrderedList, from tail to head, USING RECURSION
        For example, list with integers 1, 2, and 3 would return [3, 2, 1]"""

    def reverse_helper(self, temp) -> List:
        if temp.next == self.sentinel:
            return [temp.item]
        return self.reverse_helper(temp.next) + [temp.item]

    def size(self) -> int:
        return self.size_helper(self.sentinel)
    """Returns number of items in the OrderedList - USE RECURSION"""

    def size_helper(self, temp) -> int:
        if temp.next == self.sentinel:
            return 0
        return self.size_helper(temp.next) + 1
