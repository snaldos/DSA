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

                # adjacent vertices don't need to be checked
                # if i == j, dist[i][j] = min(0, dist[i][k] + dist[k][j]) - remains the same (0)
                # if j == k, dist[i][j] = min(dist[i][j], dist[i][j] + 0) - remains the same (dist[i][j])
                # if i == k, dist[i][j] = min(dist[i][j], 0 + dist[i][j]) - remains the same (dist[i][j])
                if i == j or j == k or i == k:
                    continue

                # If the distance from i to j through k is less than the current distance, update it
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist
