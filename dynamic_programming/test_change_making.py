from change_making import change_making


def test_has_change_canonical():
    C = [1, 2, 5, 10]
    Stock = [1, 1, 1, 1]
    result, used = change_making(C, Stock, 13)
    assert result
    assert used == [1, 1, 0, 1]

    Stock2 = [1, 2, 4, 2]
    result, used = change_making(C, Stock2, 38)
    assert result
    assert used == [1, 1, 3, 2]

    Stock3 = [10, 2, 4, 2]
    result, used = change_making(C, Stock3, 10)
    assert result
    assert used == [0, 0, 0, 1]


def test_has_change_non_canonical():
    C = [1, 4, 5]
    Stock = [2, 2, 1]

    result, used = change_making(C, Stock, 6)
    assert result
    assert used == [1, 0, 1]

    result, used = change_making(C, Stock, 8)
    assert result
    assert used == [0, 2, 0]

    Stock2 = [8, 2, 1]

    result, used = change_making(C, Stock2, 7)
    assert result
    assert used == [2, 0, 1]

    result, used = change_making(C, Stock2, 8)
    assert result
    assert used == [0, 2, 0]


def test_has_no_change():
    C = [1, 2, 5, 10]
    Stock = [0, 1, 1, 1]

    result, _ = change_making(C, Stock, 18)
    assert not result

    result, _ = change_making(C, Stock, 1)
    assert not result
