"""List utility functions."""

__author__ = "730322189"


def all(integers: list[int], match: int) -> bool:
    # Return True if all numbers match the indicated number and return False otherwise
    i: int = 0
    while i < len(integers):
        item: int = integers[i]
        if item != match:
            return False
        i += 1
        
    return True


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    # Return True if every element at every index is equal in both lists
    i: int = 0
    while i <= len(list_1) or i <= len(list_2):
        item_1: int = list_1[i]
        item_2: int = list_2[i]
        if len(list_1) != len(list_2):
            return False
        if item_1 != item_2:
            return False
        i += 1

    return True


def max(input: list[int]) -> int:
    # Return largest integer in the list
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    
    i: int = 0
    compare: int = 0
    while i < len(input):
        if input[i] > compare:
            compare = input[i]
        i += 1
    
    return compare