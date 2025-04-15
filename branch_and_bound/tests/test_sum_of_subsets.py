import pytest

from branch_and_bound.sum_of_subsets import sum_of_subsets


def sort_solutions(solutions):
    return sorted([sorted(subset) for subset in solutions])


@pytest.mark.parametrize(
    "weights, target, expected",
    [
        ([2, 3, 5, 7], 10, [[3, 7], [2, 3, 5]]),
        ([1, 2, 3], 3, [[3], [1, 2]]),
        ([1, 2, 3, 4, 5], 5, [[5], [1, 4], [2, 3]]),
        (
            [1, 1, 1, 1],
            2,
            [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],
        ),  # duplicate 1s, 4!/(2!(4-2)!) = 6 subsets of size 2
        ([10, 20, 30], 15, []),  # no subset adds to 15
        ([], 0, [[]]),  # the empty subset sums to 0
        ([], 5, []),  # no elements, no subset can reach 5
        ([1, 2, 2, 3], 4, [[1, 3], [2, 2]]),
    ],
)
def test_sum_of_subsets(weights, target, expected):
    result = sum_of_subsets(weights, target)
    assert sort_solutions(result) == sort_solutions(expected)
