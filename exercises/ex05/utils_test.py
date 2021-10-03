"""Unit tests for list utility functions."""

from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730322189"

def test_only_evens_empty() -> None:
    xs: list[int] = []
    assert only_evens(xs) == []


def test_only_evens_all_odds() -> None:
    xs: list[int] = [1, 3, 5]
    assert only_evens(xs) == []


def test_only_evens_all_evens() -> None:
    xs: list[int] = [2, 4, 6]
    assert only_evens(xs) == [2, 4, 6]


def test_sub_empty() -> None:
    xs: list[int] = []
    start: int = 1
    end: int = 3
    assert sub(xs, 1, 3) == []


def test_sub_use_case_1() -> None:
    xs: list[int] = [10, 20, 30]
    start: int = 1
    end: int = 4
    assert sub(xs, 1, 4) == [20, 30]


def test_sub_use_case_2() -> None:
    xs: list[int] = [17, 39, 4, 763, 9]
    start: int = 2
    end: int = 4
    assert sub(xs, 2, 4) == [4, 763]


def test_concat_empty() -> None:
    list_1: list[int] = []
    list_2: list[int] = []
    assert concat(list_1, list_2) == []


def test_concat_use_case_1() -> None:
    list_1: list[int] = [1, 2, 4]
    list_2: list[int] = [5, 2, 9]
    assert concat(list_1, list_2) == [1, 2,4, 5, 2, 9]


def test_concat_use_case_2() -> None:
    list_1: list[int] = [2, 4, 2]
    list_2: list[int] = [-4, -2, -90]
    assert concat(list_1, list_2) == [2, 4, 2, -4, -2, -90]