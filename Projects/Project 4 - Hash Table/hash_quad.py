from typing import List, Any, Optional

class HashTable:

    def __init__(self, table_size: int):            # can add additional attributes
        self.table_size = table_size                # initial table size
        self.hash_table: List = [None]*table_size   # hash table
        self.num_items = 0                          # empty hash table

    def insert(self, key: str, value: Any) -> None:
        self.num_items += 1
        if self.get_load_factor() > 0.5:
            self.resize_hash()
        hash_index = self.horner_hash(key)
        i = 0
        while hash_index + i*i < self.table_size:
            cur_index = hash_index + i*i
            if self.hash_table[cur_index] is None:
                self.hash_table[cur_index] = (key, value)
                hash_index = self.table_size
            elif self.hash_table[cur_index][0] == key:
                self.hash_table[cur_index] = (key, value)
                hash_index = self.table_size
            i += 1
        """ Inserts an entry into the hash table (using Horner hash function to determine index, 
        and quadratic probing to resolve collisions).
        The key is a string (a word) to be entered, and value is any object (e.g. Python List).
        If the key is not already in the table, the key is inserted along with the associated value
        If the key is is in the table, the new value replaces the existing value.
        When used with the concordance, value is a Python List of line numbers.
        If load factor is greater than 0.5 after an insertion, hash table size should be increased (doubled + 1)."""

    def resize_hash(self) -> None:
        temp_hash: List = [None] * self.table_size
        temp_num_items = self.num_items
        for i in range(self.table_size):
            temp_hash[i] = self.hash_table[i]
        for i in range(self.table_size):
            self.hash_table[i] = None
        self.table_size = self.table_size * 2 + 1
        while len(self.hash_table) < self.table_size:
            self.hash_table.append(None)
        for i in range(len(temp_hash)):
            if temp_hash[i] is not None:
                self.insert(temp_hash[i][0], temp_hash[i][1])
        self.num_items = temp_num_items


    def horner_hash(self, key: str) -> int:
        sum = 0
        if str != "":
            n = 8
            if len(key) < n:
                n = len(key)
            for i in range(n):
                sum += ord(key[i]) * pow(31, n-1-i)
        return sum % self.table_size
        """ Compute and return an integer from 0 to the (size of the hash table) - 1
        Compute the hash value by using Horner’s rule, as described in project specification."""

    def in_table(self, key: str) -> bool:
        hash_index = self.horner_hash(key)
        i = 0
        while hash_index + i*i < self.table_size:
            cur_index = hash_index + i*i
            if self.hash_table[cur_index] is None:
                return False
            elif self.hash_table[cur_index][0] == key:
                return True
            i += 1
        return False

        """ Returns True if key is in an entry of the hash table, False otherwise. Must be O(1)."""

    def get_index(self, key: str) -> Optional[int]:
        hash_index = self.horner_hash(key)
        i = 0
        while hash_index + i*i < self.table_size:
            cur_index = hash_index + i*i
            if self.hash_table[cur_index] is None:
                return None
            elif self.hash_table[cur_index][0] == key:
                return cur_index
            i += 1
        return None
        """ Returns the index of the hash table entry containing the provided key. 
        If there is not an entry with the provided key, returns None. Must be O(1)."""

    def get_all_keys(self) -> List:
        """ Returns a Python list of all keys in the hash table."""
        ret_list: List = []
        for i in range(self.table_size):
            if self.hash_table[i] is not None:
                ret_list.append(self.hash_table[i][0])
        return ret_list

    def get_value(self, key: str) -> Any:
        index = self.get_index(key)
        if index is None:
            return None
        else:
            return self.hash_table[index][1]
        """ Returns the value (for concordance, list of line numbers) associated with the key.
        If key is not in hash table, returns None. Must be O(1)."""

    def get_num_items(self) -> int:
        return self.num_items
        """ Returns the number of entries (words) in the table. Must be O(1)."""

    def get_table_size(self) -> int:
        return self.table_size
        """ Returns the size of the hash table."""

    def get_load_factor(self) -> float:
        return self.num_items/self.table_size
        """ Returns the load factor of the hash table (entries / table_size)."""

