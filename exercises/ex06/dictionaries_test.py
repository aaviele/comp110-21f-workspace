"""Unit tests for dictionary functions."""

from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "123456789"


def test_inverse_empty() -> None:
    """Test for invert, empty string."""
    given: dict[str, str] = {}
    assert invert(given) == {}


def test_invert_case_1() -> None:
    """Test for invert, use case 1."""
    given: dict[str, str] = {'apple': 'cat'}
    assert invert(given) == {'cat': 'apple'}


def test_inverse_case_2() -> None:
    """Test for invert, use case 2."""
    given: dict[str, str] = {'mustard': 'ketchup'}
    assert invert(given) == {'ketchup': 'mustard'}


def test_favorite_color_tie() -> None:
    """Test for favorite_color for tie for favorite."""
    names_and_colors: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(names_and_colors) == 'blue'


def test_favorite_colors_case_1() -> None:
    """Test for favorite_color, use case 1."""
    names_and_colors: dict[str, str] = {"Aaviele": "blue", "Kaitlyn": "green", "Sarah": "green"}
    assert favorite_color(names_and_colors) == "green"


def test_favorite_colors_case_2() -> None:
    """Test for favorite_color, use case 2."""
    names_and_colors: dict[str, str] = {"Heather": "yellow", "Jon": "green", "Bob": "yellow", "Helen": "green"}
    assert favorite_color(names_and_colors) == "yellow"


def test_count_empty() -> None:
    """Test for count if empty."""
    freq: list[str] = []
    assert count(freq) == {}


def test_count_case_1() -> None:
    """Test for count, use case 1."""
    freq: list[str] = ['blue', 'yellow', 'yellow']
    assert count(freq) == {'blue': 1, 'yellow': 2}


def test_count_case_2() -> None:
    """Test for count, use case 2."""
    freq: list[str] = ['purple', 'green', 'pink', 'green']
    assert count(freq) == {'purple': 1, 'green': 2, 'pink': 1}