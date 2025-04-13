from typing import Dict, Tuple

import pytest

from brute_force.knapsack import (  # Adjust import based on your project structure
    fractional_knapsack, knapsack01)


# Test cases for knapsack01
def test_knapsack01():
    items = {
        "item1": (3, 2),  # (value, weight)
        "item2": (4, 3),
        "item3": (5, 4),
        "item4": (6, 5),
    }
    capacity = 5
    expected_max_value = 7
    expected_selected_items = [
        {"item1": (3, 2)},
        {"item2": (4, 3)},
    ]
    max_value, selected_items = knapsack01(items, capacity)
    assert max_value == expected_max_value
    assert selected_items == expected_selected_items


def test_knapsack01_empty():
    items = {}
    capacity = 10
    expected_max_value = 0
    expected_selected_items = []
    max_value, selected_items = knapsack01(items, capacity)
    assert max_value == expected_max_value
    assert selected_items == expected_selected_items


def test_knapsack01_single_item_fits():
    items = {"item1": (5, 4)}
    capacity = 5
    expected_max_value = 5
    expected_selected_items = [{"item1": (5, 4)}]
    max_value, selected_items = knapsack01(items, capacity)
    assert max_value == expected_max_value
    assert selected_items == expected_selected_items


def test_knapsack01_single_item_does_not_fit():
    items = {"item1": (5, 6)}
    capacity = 5
    expected_max_value = 0
    expected_selected_items = []
    max_value, selected_items = knapsack01(items, capacity)
    assert max_value == expected_max_value
    assert selected_items == expected_selected_items


# Test cases for fractional_knapsack
def test_fractional_knapsack():
    items = {
        "item1": (60, 10),  # (value, weight)
        "item2": (100, 20),
        "item3": (120, 30),
    }
    capacity = 50
    expected_total_value = 240.0
    expected_selected_items = [
        {"item1": (60, 10)},
        {"item2": (100, 20)},
        {"item3": (80, 20)},
    ]
    total_value, selected_items = fractional_knapsack(items, capacity)
    assert total_value == expected_total_value
    assert selected_items == expected_selected_items


def test_fractional_knapsack_empty():
    items = {}
    capacity = 10
    expected_total_value = 0
    expected_selected_items = []
    total_value, selected_items = fractional_knapsack(items, capacity)
    assert total_value == expected_total_value
    assert selected_items == expected_selected_items


def test_fractional_knapsack_single_item_fits():
    items = {"item1": (60, 10)}
    capacity = 10
    expected_total_value = 60
    expected_selected_items = [{"item1": (60, 10)}]
    total_value, selected_items = fractional_knapsack(items, capacity)
    assert total_value == expected_total_value
    assert selected_items == expected_selected_items


def test_fractional_knapsack_single_item_does_not_fit():
    items = {"item1": (60, 15)}
    capacity = 10
    expected_total_value = 40
    expected_selected_items = [{"item1": (40, 10)}]
    total_value, selected_items = fractional_knapsack(items, capacity)
    assert total_value == expected_total_value
    assert selected_items == expected_selected_items
