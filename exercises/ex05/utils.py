"""List utility functions part 2."""

__author__ = "730383481"


def only_evens(xs: list[int]) -> list[int]:
    """Returns a list of only even values."""
    olivia: list[int] = []
    i: int = 0 
    while i < len(xs):
        if xs[i] % 2 == 0:
            olivia.append(xs[i])
        i += 1
    return olivia


def sub(xs: list[int], a: int, b: int) -> list[int]:
    """Returns a subset of the list."""
    a_list = []
    i: int = 0
    while i < len(xs):
        if i >= a and i < b: 
            a_list.append(xs[i])
        i += 1
    return a_list


def concat(xs: list[int], ys: list[int]) -> list[int]:
    """Returns the concatted list."""
    a: list[int] = []
    i: int = 0
    while i < len(xs):
        a.append(xs[i])
        i += 1
    j: int = 0
    while j < len(ys):
        a.append(ys[j])
        j += 1 
    return a