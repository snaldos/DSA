import numpy as np
from scipy.optimize import linprog


def ilp_minimization(A, b, c, bounds):
    """
    Branch and Bound algorithm to solve integer linear programming problems.

    Args:
        A (list): Coefficient matrix for inequalities (A_ub).
        b (list): RHS vector for inequalities (b_ub).
        c (list): Coefficient vector for the objective function.
        bounds (list): Bounds for each variable as (lower, upper) tuples.

    Returns:
        tuple: (best_solution, best_w) where best_solution is a tuple (x, y) and best_w is the optimal objective value.
    """
    best_w = np.inf
    best_solution = None

    def _ilp_minimization(A, b, c, bounds):
        nonlocal best_w, best_solution

        # Solve LP relaxation
        res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method="highs")

        if not res.success:
            return  # No feasible solution in this branch

        x_relaxed, y_relaxed = res.x
        w_relaxed = res.fun  # Already minimized w = -x + 2y

        # Prune if this branch cannot improve the best solution
        if w_relaxed >= best_w:
            return

        # Check if the relaxed solution is integer
        if np.isclose(x_relaxed, round(x_relaxed)) and np.isclose(
            y_relaxed, round(y_relaxed)
        ):
            if w_relaxed < best_w:
                best_w = w_relaxed
                best_solution = (int(round(x_relaxed)), int(round(y_relaxed)))
            return

        # Choose a variable to branch on
        if not np.isclose(x_relaxed, round(x_relaxed)):
            floor_x = np.floor(x_relaxed)
            ceil_x = np.ceil(x_relaxed)

            # Left branch: x <= floor_x
            new_bounds = bounds.copy()
            new_bounds[0] = (bounds[0][0], floor_x)
            _ilp_minimization(A, b, c, new_bounds)

            # Right branch: x >= ceil_x
            new_bounds = bounds.copy()
            new_bounds[0] = (ceil_x, bounds[0][1])
            _ilp_minimization(A, b, c, new_bounds)

        elif not np.isclose(y_relaxed, round(y_relaxed)):
            floor_y = np.floor(y_relaxed)
            ceil_y = np.ceil(y_relaxed)

            # Left branch: y <= floor_y
            new_bounds = bounds.copy()
            new_bounds[1] = (bounds[1][0], floor_y)
            _ilp_minimization(A, b, c, new_bounds)

            # Right branch: y >= ceil_y
            new_bounds = bounds.copy()
            new_bounds[1] = (ceil_y, bounds[1][1])
            _ilp_minimization(A, b, c, new_bounds)

    _ilp_minimization(A, b, c, bounds)
    return best_solution, best_w
