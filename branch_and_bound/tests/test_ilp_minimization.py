import pytest

from branch_and_bound.ilp_minimization import ilp_minimization


def test_ilp_minimization():
    A = [
        [-1, 0],  # -x <= 0
        [0, -1],  # -y <= 0
        [1, 1],  # x + y <= 6
        [1, 0],  # x <= 5
        [0, 1],  # y <= 4
    ]
    b = [0, 0, 6, 5, 4]
    c = [-1, 2]  # Objective: minimize w = -x + 2y
    initial_bounds = [(0, None), (0, None)]

    best_solution, best_w = ilp_minimization(A, b, c, initial_bounds)

    # Check that the solution is correct
    assert best_solution is not None, "No solution found"

    x, y = best_solution

    # Check that the solution satisfies all constraints
    assert x >= 0
    assert y >= 0
    assert x + y <= 6
    assert x <= 5
    assert y <= 4

    # Check that the solution is the known optimal solution
    assert (x, y) == (5, 0), f"Expected (5,0), got ({x},{y})"

    # Check that the objective value is correct
    expected_z = -5 + 2 * 0  # = -5
    actual_z = -x + 2 * y
    assert pytest.approx(actual_z, abs=1e-6) == expected_z
    assert pytest.approx(best_w, abs=1e-6) == expected_z
