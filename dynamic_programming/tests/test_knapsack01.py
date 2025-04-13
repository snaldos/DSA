# test_knapsack01.py

import pytest

from dynamic_programming.knapsack01 import knapsack01


def test_knapsack01_basic():
    items = {
        "item1": (3, 2),  # value, weight
        "item2": (4, 3),
        "item3": (5, 4),
        "item4": (6, 5),
    }
    capacity = 5
    max_value, selected = knapsack01(items, capacity)
    assert max_value == 7  # item1 + item2
    total_weight = sum(v[1] for i in selected for v in i.values())
    assert total_weight <= capacity


def test_knapsack01_empty_items():
    items = {}
    capacity = 10
    max_value, selected = knapsack01(items, capacity)
    assert max_value == 0
    assert selected == []


def test_knapsack01_zero_capacity():
    items = {
        "item1": (3, 2),
        "item2": (4, 3),
    }
    capacity = 0
    max_value, selected = knapsack01(items, capacity)
    assert max_value == 0
    assert selected == []


def test_knapsack01_exact_fit():
    items = {
        "item1": (10, 5),
        "item2": (40, 4),
        "item3": (30, 6),
        "item4": (50, 3),
    }
    capacity = 7
    max_value, selected = knapsack01(items, capacity)
    assert max_value == 90  # item2 + item4
    total_weight = sum(v[1] for i in selected for v in i.values())
    assert total_weight <= capacity
