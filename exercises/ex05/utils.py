"""List utility functions part 2."""

__author__ = "730322189"

def only_evens(xs: list[int]) -> list[int]:
    """Return only even numbers."""
    i: int = 0
    evens: list[int] = []
    while i < len(xs):
        if xs[i] % 2 == 0:
            evens.append(xs[i])
        i += 1
    return evens


def sub(xs: list[int], start: int, end: int) -> list[int]:
    """Generate list between start and end indices."""
    subset: list[int] = []
    if len(xs) <= 0 or start > len(xs) or end <= 0:
        return subset
    if start < 0:
        start = 0
    i: int = start
    if end > len(xs) - 1:
        end = len(xs) - 1
        while i <= end:
            subset.append(xs[i])
            i += 1
        return subset
    else:
        while i < end:
            subset.append(xs[i])
            i += 1
        return subset


def concat(list_1: list[int], list_2: list[int]) -> list[int]:
    """Return list containing items from both lists."""
    concat: list[int] = list_1
    i: int = 0
    while i < len(list_2):
        concat.append(list_2[i])
        i += 1
    return concat