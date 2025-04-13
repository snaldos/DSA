# test_subsets.py

import pytest

from brute_force.subsets import get_all_subsets, get_all_subsets_bitwise


def test_get_all_subsets_empty():
    assert get_all_subsets([]) == [[]]


def test_get_all_subsets_basic():
    result = get_all_subsets([1, 2])
    expected = [[], [2], [1], [1, 2]]
    assert sorted(result) == sorted(expected)


def test_get_all_subsets_three_elements():
    result = get_all_subsets([1, 2, 3])
    expected = [
        [],
        [3],
        [2],
        [2, 3],
        [1],
        [1, 3],
        [1, 2],
        [1, 2, 3],
    ]
    assert sorted(result) == sorted(expected)


def test_get_all_subsets_bitwise_matches_recursive():
    input_list = [1, 2, 3]
    recursive_subsets = get_all_subsets(input_list)
    bitwise_subsets = get_all_subsets_bitwise(input_list)
    assert sorted(recursive_subsets) == sorted(bitwise_subsets)
