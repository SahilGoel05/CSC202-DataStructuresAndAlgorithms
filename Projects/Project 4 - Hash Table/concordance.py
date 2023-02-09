from typing import Any, List, Optional
from hash_quad import *
import string

class Concordance:

    def __init__(self) -> None:
        """ Starting size of hash table should be 191: self.concordance_table = HashTable(191) """
        self.stop_table: Optional[HashTable] = None          # hash table for stop words
        self.concordance_table: HashTable = HashTable(191)              # hash table for concordance

    def load_stop_table(self, filename: str) -> None:
        self.stop_table = HashTable(191)
        try:
            temp_read_file = open(filename, "r")
        except FileNotFoundError:
            raise FileNotFoundError("File can not be found")
        while self.has_line(temp_read_file):
            line = temp_read_file.readline().strip("\n")
            self.stop_table.insert(line, "def")
        temp_read_file.close();

    def has_line(self, file: Any) -> bool:
        pos = file.tell()
        ret = bool(file.readline())
        file.seek(pos)
        return ret
        """ Read stop words from input file (filename) and insert each word as a key into the stop words hash table.
        Starting size of hash table should be 191: self.stop_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""

    def load_concordance_table(self, filename: str) -> None:
        try:
            temp_read_file = open(filename, "r")
        except FileNotFoundError:
            raise FileNotFoundError("File can not be found")

        line_num = 1
        while self.has_line(temp_read_file):
            line = temp_read_file.readline().strip("\n")
            line = line.lower()
            current_line:List = []
            temp = ""
            for i in range(len(line)):
                if line[i] == "'":
                    pass
                elif line[i].isalpha():
                    temp += line[i]
                elif temp != "":
                    current_line.append(temp)
                    temp = ""
            if temp != "":
                current_line.append(temp)
                temp = ""

            for i in range(len(current_line)):
                if not self.stop_table.in_table(current_line[i]):
                    value_taken = self.concordance_table.get_value(current_line[i])

                    if value_taken is None:
                        value:List = [line_num]
                        self.concordance_table.insert(current_line[i], value)
                    else:
                        skip = False
                        for j in range(len(value_taken)):
                            if line_num == value_taken[j]:
                                skip = True
                        if not skip:
                            value_taken.append(line_num)
                            self.concordance_table.insert(current_line[i], value_taken)
            for i in range(len(current_line)):
                current_line[i] = None
            line_num += 1
        temp_read_file.close();
        """ Read words from input text file (filename) and insert them into the concordance hash table, 
        after processing for punctuation, numbers and filtering out words that are in the stop words hash table.
        Do not include duplicate line numbers (word appearing on same line more than once, just one entry for that line)

        Process of adding new line numbers for a word (key) in the concordance:
            If word is in table, get current value (list of line numbers), append new line number, insert (key, value)
            If word is not in table, insert (key, value), where value is a Python List with the line number
        If file does not exist, raise FileNotFoundError """

    def write_concordance(self, filename: str) -> None:
        temp_list = self.concordance_table.get_all_keys()
        temp_list.sort()
        temp_write_file = open(filename, "w")
        for i in range(len(temp_list)):
            value = self.concordance_table.get_value(temp_list[i])
            temp_write_file.write(temp_list[i] + ": ")
            for j in range(len(value)):
                if j == len(value) - 1:
                    temp_write_file.write(str(value[j]))
                else:
                    temp_write_file.write(str(value[j]) + " ")
            temp_write_file.write("\n")
        temp_write_file.close()
        """ Write the concordance entries to the output file(filename)
        See sample output files for format. """
