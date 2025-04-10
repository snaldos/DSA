def floyd_warshall(graph):
    """
    Computes the shortest distances between every pair of vertices in the graph using the Floyd–Warshall algorithm.

    Parameters:
        graph (list of lists): A 2D list where graph[i][j] is the weight of the edge from i to j,
                               or float('inf') if no such edge exists. A zero on the diagonal implies
                               no self-loop cost.

    Returns:
        list of lists: A 2D list where the entry at [i][j] is the minimum distance from vertex i to vertex j.
    """
    # Number of vertices in the graph
    n = len(graph)

    # Initialize the distance matrix with the input graph values (deep copy)
    dist = [row[:] for row in graph]

    # Dynamic programming: iteratively improve the solution by considering each vertex as an intermediate point.
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # Ensure no invalid updates when paths involve INF
                if dist[i][k] != float("inf") and dist[k][j] != float("inf"):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist
