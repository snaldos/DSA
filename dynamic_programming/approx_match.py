import os
from typing import List


def edit_distance(pattern: str, text: str) -> int:
    m, n = len(pattern), len(text)
    dp: List[List[int]] = [[0] * (n + 1) for _ in range(m + 1)]

    # deleting all characters from pattern
    for i in range(m + 1):
        dp[i][0] = i

    # inserting all characters from text
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if pattern[i - 1] == text[j - 1]:
                # characters match, no operation needed
                dp[i][j] = dp[i - 1][j - 1]
            else:
                # characters do not match, consider all possibilities
                # 1. insert
                # 2. delete
                # 3. replace
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

    return dp[m][n]


def num_approximate_string_matching(filename: str, to_search: str) -> float:
    if not os.path.exists(filename):
        print("Error opening file.")
        return -1

    total_distance = 0
    word_count = 0

    with open(filename, "r") as file:
        for word in file.read().split():
            total_distance += edit_distance(to_search, word)
            word_count += 1

    return total_distance / word_count if word_count > 0 else -1
