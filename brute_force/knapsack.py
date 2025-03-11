from typing import Dict, List, Tuple

from subsets import get_all_subsets


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
            total_value += item[1][2] * capacity
            selected_items.append({item[0]: (item[1][0], capacity)})
            capacity = 0

    return total_value, selected_items


"""Code Testing
"""


if __name__ == "__main__":
    # KnapSack 0/1
    # Example usage:
    items = {
        "item1": (3, 2),  # (value, weight)
        "item2": (4, 3),
        "item3": (5, 4),
        "item4": (6, 5),
    }
    capacity = 5

    max_value, selected_items = knapsack01(items, capacity)

    print("Maximum Value:", max_value)
    print("Items Selected:", selected_items)

    # Fractional KnapSack
    # Example usage:
    items = {
        "item1": (60, 10),
        "item 2": (100, 20),
        "item 3": (120, 30),
    }  # (value, weight)
    capacity = 50

    max_value, selected_items = fractional_knapsack(items, capacity)

    print("Maximum Value:", max_value)
    print("Items Selected:", selected_items)
