# test_max_subsequence.py

import pytest

from brute_force.max_subsequence import max_subsequence, max_subsequence_bf


@pytest.mark.parametrize(
    "nums, expected_sum, expected_range",
    [
        ([53, -72, -90, -55, -37, 99, -78, 24, 7, 5], 99, (5, 5)),
        ([-48, -20, -40, -60, -82, 97, 37, 0, -99, -1], 134, (5, 6)),
        ([53, -69, 3, 51, 62, 13, 81, -74, 33, -93], 210, (2, 6)),
        ([-1, -2, -3], -1, (0, 0)),
        ([1, 2, 3, 4], 10, (0, 3)),
        ([1, -2, 3, 5, -1, 2], 9, (2, 5)),
    ],
)
def test_max_subsequence_bf_and_clever(nums, expected_sum, expected_range):
    index_bf = [0, 0]
    index_kadane = [0, 0]

    sum_bf = max_subsequence_bf(nums, index_bf)
    sum_kadane = max_subsequence(nums, index_kadane)

    assert sum_bf == expected_sum
    assert tuple(index_bf) == expected_range

    assert sum_kadane == expected_sum
    assert tuple(index_kadane) == expected_range
