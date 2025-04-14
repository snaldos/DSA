def transitive_closure(graph):
    """
    Computes the transitive closure of a directed graph using the Floyd-Warshall algorithm.

    Parameters:
        graph (list of lists): A 2D list where graph[i][j] is True if there is a direct edge from i to j,
                                or False if no such edge exists. A zero on the diagonal implies
                                no self-loop cost.

    Returns:
        list of lists: A 2D list where the entry at [i][j] is True if there is a path from vertex i to vertex j.
    """
    # Number of vertices in the graph
    n = len(graph)

    # Initialize the reachability matrix with the input graph values (deep copy)
    reach = [row[:] for row in graph]

    # following the convention "every node is reachable from itself"
    # for i in range(n):
    #     reach[i][i] = True

    # Dynamic programming: iteratively improve the solution by considering each vertex as an intermediate point.
    for k in range(n):
        for i in range(n):
            for j in range(n):

                # Optimization: skipping cases where updates are guaranteed to be no-ops
                # (Optional: classic Floyd–Warshall doesn't skip these)
                # if i == j, reach[i][j] = min(0, reach[i][k] + reach[k][j]) - remains the same (0)
                # if j == k, reach[i][j] = min(reach[i][j], reach[i][j] + 0) - remains the same (reach[i][j])
                # if i == k, reach[i][j] = min(reach[i][j], 0 + reach[i][j]) - remains the same (reach[i][j])
                if i == j or j == k or i == k:
                    continue
                # If there is a path from i to k and from k to j, then there is a path from i to j
                reach[i][j] = reach[i][j] or (reach[i][k] and reach[k][j])

    return reach
