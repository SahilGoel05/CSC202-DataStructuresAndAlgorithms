from __future__ import annotations
# NodeList version of ADT Queue

from typing import Optional, List, Any

# Node class for use with Queue implemented with linked list
# NodeList is one of
# None or
# Node(value, rest), where rest is the rest of the list
class Node:
    def __init__(self, value: Any, rest: Optional[Node]):
        self.value = value      # value
        self.rest = rest        # NodeList

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Node):
            return self.value == other.value and self.rest == other.rest
        else:
            return False

    def __repr__(self) -> str:
        return ("Node({!r}, {!r})".format(self.value, self.rest))

class Queue:
    def __init__(self, rear: Optional[Node] = None, front: Optional[Node] = None, num_items: int = 0):
        self.rear = rear    # rear NodeList
        self.front = front   # front NodeList
        self.num_items = num_items  # number of items in Queue

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Queue):
            return self.get_items() == other.get_items()
        else:
            return False

    def __repr__(self) -> str:
        return ("Queue({!r}, {!r})".format(self.rear, self.front))

    # get_items returns array (Python list) of items in Queue
    # first item in the list will be front of queue, last item is rear of queue
    def get_items(self) -> List:
        items: List = []
        front = self.front
        while front is not None:
            items.append(front.value)
            front = front.rest
        if self.rear is not None:
            rear_items = []
            rear: Optional[Node] = self.rear
            while rear is not None:
                rear_items.append(rear.value)
                rear = rear.rest
            rear_items.reverse()
            items.extend(rear_items)
        return items

    def is_empty(self) -> bool:
        if self.front.value is None and self.rear.value is None or self.front is None and self.rear is None:
            return True
        return False
        """Returns true if the queue is empty and false otherwise
        Must be O(1)"""

    def enqueue(self, item: Any) -> None:
        if self.rear is None:
            self.rear = Node(item, None)
        else:
            tempNode = self.rear.rest
            self.rear.rest = Node(item, tempNode)
        self.num_items += 1

        """enqueues item, adding it to the rear NodeList
        Must be O(1)"""

    def dequeue(self) -> Any:
        if self.front is None:
            if self.rear is None:
                raise IndexError
            if self.front.rest is None:
                self.front.rest = Node(self.rear.value, None)
                temp = self.rear.value
                self.rear.value = None
                self.num_items -= 1
                return temp
            else:
                while self.rear.rest is not None:
                    tempRearNode = self.rear.rest
                    if self.front is None:
                        self.front = Node(tempRearNode.value, None)
                    else:
                        tempFrontNode = self.front.rest
                        self.front.rest = Node(tempRearNode.value, tempFrontNode)
                        self.rear.rest = tempRearNode.rest
                temp = self.rear.value
                self.rear.value = None
                self.num_items -= 1
                return temp
        else:
            tempNode = self.front.rest
            self.front.rest = tempNode.rest
            self.num_items -= 1
            return tempNode.value


    """dequeues item, removing first item from front NodeList
        If front NodeList is empty, remove items from rear NodeList
        and add to front NodeList until rear NodeList is empty
        (This will still satisfy O(1) requirement for the operation,
        as the transfer is amortized across all dequeues)
        If front NodeList and rear NodeList are both empty, raise IndexError
        Must be O(1) - general case"""

    def size(self) -> int:
        return self.num_items
        """Returns the number of items in the queue
        Must be O(1)"""
