# CPE 202 Lab 1a - List Manipulation
from typing import Optional
from typing import List

# Maybe_List (Optional[List]) is either
# Python List
# or
# None

# Maybe_integer (Optional[int]) is either
# integer
# or
# None

# Maybe_List -> Maybe_integer
def max_list_iter(int_list: Optional[List]) -> Optional[int]:
   if(isinstance(int_list, List)):
      if(len(int_list) != 0):
         max = int_list[0]
         for i in int_list:
            if(i > max):
               max = i
         return max
      else:
         return None
   raise ValueError

"""finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""

# Maybe_List -> Maybe_List
def reverse_list(int_list: Optional[List]) -> Optional[List]:
   if(isinstance(int_list, List)):
      reversed_list: List[int] = list()
      for i in int_list:
         reversed_list = [i] + reversed_list
      return reversed_list
   raise ValueError

"""reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""

# Maybe_List -> None
def reverse_list_mutate(int_list: Optional[List]) -> None:
   if(isinstance(int_list, List)):
      for i in range(len(int_list) // 2):
         int_list[i], int_list[-1 - i] = int_list[-1 - i], int_list[i]
   else:
      raise ValueError

   """reverses a list of numbers, modifying the input list, returns None
   If list is None, raises ValueError"""
