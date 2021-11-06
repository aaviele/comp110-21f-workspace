"""Utility functions."""

__author__ = "730322189"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []

    file_handle = open(filename, "r", encoding="utf8")
    
    csv_reader = DictReader(file_handle)

    for row in csv_reader:
        result.append(row)

    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(col_based: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Produce a new column-based table with only the first N rows of data for each column."""
    result: dict[str, list[str]] = {}
    
    if rows < len(col_based):
        for key in col_based:
            store: list[str] = []
            i: int = 0
            while i < rows:
                store.append(col_based[key][i])
                i += 1
            result[key] = store
        
    else:
        result = col_based

    return result


def select(data_cols: dict[str, list[str]], column_names: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    for name in column_names:
        result[name] = data_cols[name]
    return result


def concat(dict_1: dict[str, list[str]], dict_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based table with two column-based tables combine."""
    result: dict[str, list[str]] = {}
    result = dict_1
    for item in dict_2:
        if item in dict_1:
            i: int = 0
            while i < len(dict_2[item]):
                result[item].append(dict_2[item][i])
                i += 1
        else:
            result[item] = dict_2[item]

    return result


def count(frequency_count: list[str]) -> dict[str, int]:
    """Produce a dictionary counting number of appearances for each unique value."""
    result: dict[str, int] = {}
    for value in frequency_count:
        if value in result:
            result[value] += 1
        else:
            result[value] = 1
    return result