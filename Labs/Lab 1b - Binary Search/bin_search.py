# CPE 202 Lab 1b - Binary Search
from typing import List, Optional

# Binary Search using iteration
# Python List (or None), number -> number or None
def bin_search_iter(int_list: Optional[List], target: int) -> Optional[int]:
    """ searches for target in int_list and returns associated index if found, otherwise returns None
        int_list must be in ascending order for Binary Search to return proper result
        if int_list is None, raise ValueError"""
    if int_list is None:
        raise ValueError
    low = 0
    high = len(int_list) - 1
    while low <= high:  # Corrected the error: changed from "<" to "<="
        mid = (high + low) // 2
        if int_list[mid] < target:  # If mid value is less than target, ignore left half
            low = mid + 1
        elif int_list[mid] > target:  # If mid value is greater than target, ignore right half
            high = mid - 1
        else:  # mid value must equal target
            return mid
    # If we reach here, target not present
    return None

# Binary Search using recursion
# Python List (or None), number -> number or None
def bin_search_rec(int_list: Optional[List], target: int) -> Optional[int]:
    """ searches for target in int_list and returns associated index if found, otherwise returns None
        int_list must be in ascending order for Binary Search to return proper result
        if int_list is None, raise ValueError"""
    if int_list is None:
        raise ValueError

    return bin_search_rec_helper(int_list, target, 0, len(int_list)-1)

# Recursive helper function
# Python List, number, number, number -> number or None
def bin_search_rec_helper(int_list: List, target: int, low: int, high: int) -> Optional[int]:
    """ searches for target in int_list[low..high] and returns index if found"""
    if len(int_list) == 0:
        return None

    mid = (low + high) // 2

    if low == high:
        if int_list[mid] == target:
            return mid
        return None
    elif int_list[mid] < target:
        return bin_search_rec_helper(int_list, target, mid + 1, high)
    elif int_list[mid] > target:
        return bin_search_rec_helper(int_list, target, low, mid - 1)
    return mid
    # Don't need to check for

