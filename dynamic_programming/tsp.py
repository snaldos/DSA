import sys


def tsp(graph):
    n = len(graph)
    VISITED_ALL = (1 << n) - 1
    memo = [[-1] * (1 << n) for _ in range(n)]
    parent = [[-1] * (1 << n) for _ in range(n)]

    def _tsp(pos, visited):
        if visited == VISITED_ALL:
            return graph[pos][0]  # return to starting city

        if memo[pos][visited] != -1:
            return memo[pos][visited]

        min_cost = sys.maxsize
        for city in range(n):
            if not visited & (1 << city):
                new_visited = visited | (1 << city)
                cost = graph[pos][city] + _tsp(city, new_visited)
                if cost < min_cost:
                    min_cost = cost
                    # Stores which next city gave the optimal path from (pos, visited)
                    parent[pos][visited] = city

        # Caches the minimum cost from city pos having visited the set visited.
        memo[pos][visited] = min_cost
        return min_cost

    total_cost = _tsp(0, 1)

    # Reconstruct the path
    path = [0]
    visited = 1
    current = 0
    while True:
        next_city = parent[current][visited]
        if next_city == -1:
            break
        path.append(next_city)
        visited |= 1 << next_city
        current = next_city
    path.append(0)  # return to start

    return total_cost, path


if __name__ == "__main__":
    graph = [
        [0, 4, 1],  # From city 0 to 1 = 4, to 2 = 1
        [2, 0, 5],  # From city 1 to 0 = 2, to 2 = 5
        [3, 1, 0],  # From city 2 to 0 = 3, to 1 = 1
    ]
    cost, path = tsp(graph)
    print(f"Minimum cost: {cost}")
    print(f"Path: {path}")
