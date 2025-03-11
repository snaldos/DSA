from typing import Dict, Tuple, List

"""
Given a list of items with values and weights, as well as a maximum weight, find the maximum value you can generate by selecting items such that the sum of the weights is less than or equal to the maximum.

This problem can be solved by brute forcing all possible combinations of items (just like the subset generator function). 

Another solution for the knapsack problem would be by using dynamic programming.
Understanding this solution requires prior knowledge on a DP table.
"""


# Dynamic programming solution to the 0/1 knapsack problem
def knapsack01(
    items: Dict[str, Tuple[int, int]], capacity: int
) -> Tuple[int, List[Dict[str, Tuple[int, int]]]]:
    values = [item[0] for item in items.values()]
    weights = [item[1] for item in items.values()]
    items_names = list(items.keys())

    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] > w:
                dp[i][w] = dp[i - 1][w]
            else:
                dp[i][w] = max(
                    dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]]
                )

    selected_items: List[Dict[str, Tuple[int, int]]] = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append({items_names[i - 1]: (values[i - 1], weights[i - 1])})
            w -= weights[i - 1]

    selected_items.reverse()
    return dp[n][capacity], selected_items


if __name__ == "__main__":
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

