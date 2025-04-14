import pytest

from dynamic_programming.transitive_closure import transitive_closure


def test_empty_graph():
    graph = []
    expected = []
    assert transitive_closure(graph) == expected


def test_single_node_self_loop():
    graph = [[True]]  # diagonal True
    expected = [[True]]
    assert transitive_closure(graph) == expected


def test_single_node_with_self_loop():
    graph = [[True]]
    expected = [[True]]
    assert transitive_closure(graph) == expected


def test_two_nodes_one_direction():
    graph = [[True, True], [False, True]]
    expected = [[True, True], [False, True]]
    assert transitive_closure(graph) == expected


def test_two_nodes_bidirectional():
    graph = [[True, True], [True, True]]
    expected = [[True, True], [True, True]]
    assert transitive_closure(graph) == expected


def test_chain():
    # 0 -> 1 -> 2
    graph = [
        [True, True, False],
        [False, True, True],
        [False, False, True],
    ]
    expected = [
        [True, True, True],
        [False, True, True],
        [False, False, True],
    ]
    assert transitive_closure(graph) == expected


def test_cycle():
    # 0 -> 1 -> 2 -> 0
    graph = [
        [True, True, False],
        [False, True, True],
        [True, False, True],
    ]
    expected = [
        [True, True, True],
        [True, True, True],
        [True, True, True],
    ]
    assert transitive_closure(graph) == expected


def test_disconnected_components():
    graph = [
        [True, True, False, False],
        [False, True, False, False],
        [False, False, True, True],
        [False, False, False, True],
    ]
    expected = [
        [True, True, False, False],
        [False, True, False, False],
        [False, False, True, True],
        [False, False, False, True],
    ]
    assert transitive_closure(graph) == expected


def test_fully_connected_graph():
    graph = [
        [True, True, True],
        [True, True, True],
        [True, True, True],
    ]
    expected = [
        [True, True, True],
        [True, True, True],
        [True, True, True],
    ]
    assert transitive_closure(graph) == expected
