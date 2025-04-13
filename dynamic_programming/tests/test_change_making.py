# test_change_making.py

import pytest

from dynamic_programming.change_making import change_making


def test_change_making_basic():
    C = [1, 2, 5]
    Stock = [5, 2, 2]
    T = 11
    result, coins = change_making(C, Stock, T)
    assert result is True
    assert sum(c * n for c, n in zip(C, coins)) == T
    assert all(used <= avail for used, avail in zip(coins, Stock))


def test_change_making_exact_stock_limit():
    C = [1, 2, 5]
    Stock = [1, 1, 1]
    T = 8  # 5 + 2 + 1
    result, coins = change_making(C, Stock, T)
    assert result is True
    assert coins == [1, 1, 1]


def test_change_making_impossible():
    C = [2, 5]
    Stock = [1, 1]
    T = 1  # Can't make 1 with 2s and 5s
    result, coins = change_making(C, Stock, T)
    assert result is False
    assert coins == [0, 0]


def test_change_making_zero_target():
    C = [1, 2, 5]
    Stock = [5, 5, 5]
    T = 0
    result, coins = change_making(C, Stock, T)
    assert result is True
    assert coins == [0, 0, 0]
