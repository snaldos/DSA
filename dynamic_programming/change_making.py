import sys
import unittest


def change_making(C, Stock, T):
    n = len(C)
    # Initialize the DP table
    dp = [[sys.maxsize] * (T + 1) for _ in range(n + 1)]
    count = [[0] * (T + 1) for _ in range(n + 1)]

    # Base case: 0 amount can be made with 0 coins
    dp[0][0] = 0

    # Fill the DP table
    for i in range(1, n + 1):
        for t in range(0, T + 1):
            # If we don't take the coin
            dp[i][t] = dp[i - 1][t]
            count[i][t] = 0

            # If we take the coin
            for k in range(1, min(Stock[i - 1], t // C[i - 1]) + 1):
                if dp[i - 1][t - k * C[i - 1]] != sys.maxsize:
                    new_coins = dp[i - 1][t - k * C[i - 1]] + k
                    if new_coins < dp[i][t]:
                        dp[i][t] = new_coins
                        count[i][t] = k

    used_coins = [0] * n

    if dp[n][T] == sys.maxsize:
        return False, used_coins

    # Backtrack to find the used coins
    t = T
    for i in range(n, 0, -1):
        used_coins[i - 1] = count[i][t]
        t -= count[i][t] * C[i - 1]

    return True, used_coins
