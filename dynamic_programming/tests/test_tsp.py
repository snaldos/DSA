import pytest

from dynamic_programming.tsp import tsp


def test_tsp_example():
    graph = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
    cost, path = tsp(graph)

    assert cost == 80

    # Allow either of the two optimal paths
    valid_paths = [[0, 1, 3, 2, 0], [0, 2, 3, 1, 0]]
    assert path in valid_paths
