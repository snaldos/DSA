# test_floyd_warshall.py

import pytest

from dynamic_programming.floyd_warshall import floyd_warshall


def test_floyd_warshall_basic():
    INF = float("inf")
    graph = [[0, 3, INF, 5], [2, 0, INF, 4], [INF, 1, 0, INF], [INF, INF, 2, 0]]
    expected = [[0, 3, 7, 5], [2, 0, 6, 4], [3, 1, 0, 5], [5, 3, 2, 0]]
    result = floyd_warshall(graph)
    assert result == expected


def test_floyd_warshall_empty():
    assert floyd_warshall([]) == []


def test_floyd_warshall_single_node():
    assert floyd_warshall([[0]]) == [[0]]
