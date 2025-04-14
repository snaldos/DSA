def sum_of_subsets(weights, target):
    """
    Finds all subsets of the given list of weights that sum up to the target value.

    This function uses the branch-and-bound technique to efficiently explore
    subsets of the input list. It prunes branches of the search tree where
    the target cannot be achieved, either because the current sum exceeds
    the target or because the remaining weights cannot reach the target.

    Args:
        weights (list[int]): A list of positive integers representing weights.
        target (int): The target sum to achieve with subsets of weights.

    Returns:
        list[list[int]]: A list of all subsets (as lists of integers) that sum up to the target value.
                         Each subset is represented as a list of integers.

    Example:
        >>> sum_of_subsets([2, 3, 5, 7], 10)
        [[3, 7], [2, 3, 5]]
    """
    n = len(weights)
    solutions = []
    weights.sort()  # Optional but helps with pruning

    def backtrack(index, current_sum, subset, remaining_sum):
        if current_sum == target:
            solutions.append(subset[:])
            return

        if index >= n or current_sum + remaining_sum < target:
            return

        # Try including the current weight
        if current_sum + weights[index] <= target:
            subset.append(weights[index])
            backtrack(
                index + 1,
                current_sum + weights[index],
                subset,
                remaining_sum - weights[index],
            )
            subset.pop()

        # Try excluding the current weight
        backtrack(index + 1, current_sum, subset, remaining_sum - weights[index])

    backtrack(0, 0, [], sum(weights))

    return solutions
