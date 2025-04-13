from typing import Dict, List, Tuple

from brute_force.subsets import get_all_subsets


def knapsack01(
    items: Dict[str, Tuple[int, int]], capacity: int
) -> Tuple[int, List[Dict[str, Tuple[int, int]]]]:
    possibilities = get_all_subsets([(key, value) for key, value in items.items()])
    max_value = float("-inf")
    selected_items = []

    for possibility in possibilities:
        total_weight = sum([item[1][1] for item in possibility])
        if total_weight <= capacity:
            total_value = sum([item[1][0] for item in possibility])
            if total_value > max_value:
                max_value = total_value
                selected_items = [{item[0]: item[1]} for item in possibility]

    return max_value, selected_items


def fractional_knapsack(
    items: Dict[str, Tuple[int, int]], capacity: int
) -> Tuple[float, List[Dict[str, Tuple[float, int]]]]:
    sorted_items = {
        key: (value[0], value[1], value[0] / value[1]) for key, value in items.items()
    }
    sorted_items = sorted(sorted_items.items(), key=lambda x: x[1][2], reverse=True)

    total_value = 0
    selected_items = []

    for item in sorted_items:
        if capacity == 0:
            break
        if item[1][1] <= capacity:
            total_value += item[1][0]
            selected_items.append({item[0]: (item[1][0], item[1][1])})
            capacity -= item[1][1]
        else:
            fractional_value = item[1][2] * capacity
            total_value += fractional_value
            selected_items.append({item[0]: (fractional_value, capacity)})
            capacity = 0

    return total_value, selected_items
