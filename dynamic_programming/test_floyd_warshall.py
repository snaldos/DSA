# test_floyd_warshall.py

import math

import pytest
from floyd_warshall import floyd_warshall


@pytest.fixture
def INF():
    return float("inf")


def test_basic_graph(INF):
    # Create a simple graph with 4 vertices
    graph = [[0, 3, INF, 5], [2, 0, INF, 4], [INF, 1, 0, INF], [INF, INF, 2, 0]]
    expected = [[0, 3, 7, 5], [2, 0, 6, 4], [3, 1, 0, 5], [5, 3, 2, 0]]
    result = floyd_warshall(graph)
    assert result == expected


def test_no_edges(INF):
    # Test a graph with 3 vertices with no connecting edges except self loops
    graph = [[0, INF, INF], [INF, 0, INF], [INF, INF, 0]]
    expected = [[0, INF, INF], [INF, 0, INF], [INF, INF, 0]]
    result = floyd_warshall(graph)
    assert result == expected


def test_negative_weight_edge(INF):
    # Graph with negative edge weights (but no negative cycles)
    graph = [[0, 1, INF], [INF, 0, -1], [2, INF, 0]]
    expected = [[0, 1, 0], [1, 0, -1], [2, 3, 0]]
    result = floyd_warshall(graph)
    # Using math.isclose for potential floating point comparisons
    for i in range(len(graph)):
        for j in range(len(graph)):
            assert math.isclose(result[i][j], expected[i][j], rel_tol=1e-9) or (
                result[i][j] == expected[i][j]
            )


if __name__ == "__main__":
    pytest.main()
