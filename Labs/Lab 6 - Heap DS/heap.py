from typing import Any, List

class MinHeap:

    def __init__(self, capacity: int = 50):
        """Constructor creating an empty heap with default capacity = 50 but allows heaps of other capacities to be created."""
        self.heap: List = [0]*(capacity+1)     # index 0 not used for heap
        self.num_items = 0                     # empty heap

    def enqueue(self, item: Any) -> None:
        self.heap[self.num_items + 1] = item
        self.num_items += 1
        self.perc_up(self.num_items)
        """inserts "item" into the heap
        Raises IndexError if there is no room in the heap"""

    def peek(self) -> Any:
        if self.is_empty():
            raise IndexError
        return self.heap[1]
        """returns root of heap (highest priority) without changing the heap
        Raises IndexError if the heap is empty"""

    def dequeue(self) -> Any:
        if self.is_empty():
            raise IndexError
        retval = self.heap[1]
        self.heap[1] = self.heap[self.num_items]
        self.num_items = self.num_items - 1
        self.heap[self.num_items + 1] = 0
        self.perc_down(1)
        return retval

        """returns item at root (highest priority) - removes it from the heap and restores the heap property
           Raises IndexError if the heap is empty"""

    def contents(self) -> List:
        ret_list = self.heap[1: self.num_items + 1]
        return ret_list
        """returns a list of contents of the heap in the order it is stored internal to the heap.
        (This may be useful for in testing your implementation.)
        If heap is empty, returns empty list []"""

    def build_heap(self, alist: List) -> None:
        i = len(alist) // 2
        self.num_items = len(alist)
        for j in range(len(alist)):
            self.heap[j + 1] = alist[j]
        while i > 0:
            self.perc_down(i)
            i = i - 1
        self.contents()
        """Discards the items in the current heap and builds a heap from
        the items in alist using the bottom up method.
        If the capacity of the current heap is less than the number of
        items in alist, the capacity of the heap will be increased to accommodate the items in alist"""

    def is_empty(self) -> bool:
        if self.num_items == 0:
            return True
        return False
        """returns True if the heap is empty, false otherwise"""

    def is_full(self) -> bool:
        self.contents()
        if self.num_items == len(self.heap) - 1:
            return True
        return False
        """returns True if the heap is full, false otherwise"""

    def capacity(self) -> int:
        return len(self.heap) - 1
        """This is the maximum number of a entries the heap can hold, which is
        1 less than the number of entries that the array allocated to hold the heap can hold"""
    
    def size(self) -> int:
        return self.num_items

        """the actual number of elements in the heap, not the capacity"""

    def perc_down(self, i: int) -> None:
        while (i * 2) <= self.num_items:
            min_ind = self.min_child(i)
            if self.heap[i] > self.heap[min_ind]:
                tmp = self.heap[i]
                self.heap[i] = self.heap[min_ind]
                self.heap[min_ind] = tmp
            i = min_ind

    def min_child(self, i: int) -> int:
        if i * 2 + 1 > self.num_items:
            return i * 2
        else:
            if self.heap[i*2] < self.heap[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1
    """where the parameter i is an index in the heap and perc_down moves the element stored
    at that location to its proper place in the heap rearranging elements as it goes."""

    def perc_up(self, i: int) -> None:
        while i // 2 > 0:
            if self.heap[i] < self.heap[i // 2]:
                tmp = self.heap[i // 2]
                self.heap[i // 2] = self.heap[i]
                self.heap[i] = tmp
            i = i // 2
        """where the parameter i is an index in the heap and perc_up moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes."""

    def heap_sort_ascending(self, alist: List) -> None:
        temp_list = alist
        new_list = alist
        i = 0
        while len(temp_list) > 1:
            self.build_heap(temp_list)
            new_list = new_list[0: i] + self.heap[1: self.num_items + 1]
            i += 1
            temp_list = new_list[i: len(new_list)]

        for i in range(len(alist)):
            alist[i] = new_list[i]
        """perform heap sort on input alist in ascending order
        This method will discard the current contents of the heap, build a new heap using
        the items in alist, and mutate (change contents of) alist to put the items in ascending order"""
