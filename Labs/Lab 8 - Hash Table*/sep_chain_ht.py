from typing import Any, Tuple, List

class MyHashTable:

    def __init__(self, table_size: int = 11):
        self.table_size = table_size
        self.hash_table: List = [[] for _ in range(table_size)] # List of lists implementation
        self.num_items = 0
        self.num_collisions = 0

    def insert(self, key: int, value: Any) -> None:
        if key < 0:
            raise ValueError
        hash_value = key % self.table_size
        done = False
        for j in range(len(self.hash_table[hash_value])):
            if key == (self.hash_table[hash_value][j])[0] and value == (self.hash_table[hash_value][j])[1]:
                done = True
        if done is False:
            self.num_items += 1
            if self.load_factor() > 1.5:
                self.create_new_hash()
            else:
                self.hash_table[hash_value].append((key, value))
                if len(self.hash_table[hash_value]) > 1:
                    self.num_collisions += 1
        """Takes a key, and an item.  Keys are valid Python non-negative integers.
        If key is negative, raise ValueError
        The function will insert the key-item pair into the hash table based on the
        hash value of the key mod the table size (hash_value = key % table_size)"""

    def create_new_hash(self):
        temp_hash = self.hash_table
        self.hash_table: List = [[] for _ in range(self.table_size * 2 + 1)]
        temp_collisions = self.num_collisions
        temp_num_items = self.num_items
        for i in range(len(temp_hash)):
            for j in range(len(temp_hash[i])):
                self.insert((temp_hash[i][j])[0], (temp_hash[i][j])[1])
        self.num_collisions = temp_collisions
        self.num_items = temp_num_items


    def get_item(self, key: int) -> Any:
        hash_value = key % self.table_size
        if self.hash_table[hash_value] is None:
            raise LookupError
        for j in range(len(self.hash_table[hash_value])):
            if (self.hash_table[hash_value][j])[0] == key:
                return self.hash_table[hash_value][j][1]
        raise LookupError

        """Takes a key and returns the item from the hash table associated with the key.
        If no key-item pair is associated with the key, the function raises a LookupError exception."""

    def remove(self, key: int) -> Tuple[int, Any]:
        hash_value = key % self.table_size
        if self.hash_table[hash_value] is None:
            raise LookupError
        for j in range(len(self.hash_table[hash_value])):
            if (self.hash_table[hash_value][j])[0] == key:
                ret_val = self.hash_table[hash_value][j]
                self.hash_table[hash_value].pop(j)
                self.num_items = self.num_items - 1
                return ret_val

        raise LookupError
        """Takes a key, removes the key-item pair from the hash table and returns the key-item pair.
        If no key-item pair is associated with the key, the function raises a LookupError exception.
        (The key-item pair should be returned as a tuple)"""

    def load_factor(self) -> float:
        """Returns the current load factor of the hash table"""
        return self.num_items/self.table_size

    def size(self) -> int:
        """Returns the number of key-item pairs currently stored in the hash table"""
        return self.num_items

    def collisions(self) -> int:
        """Returns the number of collisions that have occurred during insertions into the hash table"""
        return self.num_collisions

