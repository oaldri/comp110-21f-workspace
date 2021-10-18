"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex05.utils import only_evens, sub, concat

__author__ = "123456789"


def test_sub_usual0() -> None:
    """Usual test for sub."""
    list1: list[int] = [10, 20, 30, 40]
    assert sub(list1, 1, 3) == [20, 30]


def test_sub_edge0() -> None:
    """Edge case for sub, empty list."""
    test1: list[int] = []
    assert sub(test1, 0, 0) == []


def test_sub_use() -> None: 
    """Standard use for sub."""
    test1: list[int] = [10, 15, 20, 25]
    assert sub(test1, -1, 2) == [10, 15]


def test_concat_use() -> None:
    """Regular concat test."""
    a_list: list[int] = [1, 2, 3, 4]
    b_list: list[int] = [5, 6]
    assert concat(a_list, b_list) == [1, 2, 3, 4, 5, 6]


def test_concat_edge() -> None: 
    """One empty list edge case using concat."""
    listA: list[int] = []
    listB: list[int] = [1, 2, 3]
    assert concat(listA, listB) == [1, 2, 3]


def test_concat_use2() -> None: 
    """Regular concat test using negatives."""
    list_1: list[int] = [-1, -2, -3]
    list2: list[int] = [-4, -5, -6]
    assert concat(list_1, list2) == [-1, -2, -3, -4, -5, -6]


def test_only_evens_use() -> None:
    """Regular only even test."""
    a_list: list[int] = [1, 2, 3, 4]
    assert only_evens(a_list) == [2, 4]


def test_only_evens_edge() -> None: 
    """Only even edge case with an empty list."""
    a_list: list[int] = []
    assert only_evens(a_list) == []


def test_only_evens_use2() -> None: 
    """Test case for only evens."""
    a_list: list[int] = [1, 3, 6, 10]
    assert only_evens(a_list) == [6, 10]