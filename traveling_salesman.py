from typing import List
coords = list[int, int]

# Euclidean path
def dist(A: coords, B: coords) -> float:
    return ((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2) ** (1/2)

# Generates all permutations
def permute(A, i, res):
    _A = [i for i in A]
    n = len(_A)
    if i == n:
        res.append(_A)
    for j in range(i, n):
        _A[i], _A[j] = _A[j], _A[i]
        permute(_A, i + 1, res)
        _A[i], _A[j] = _A[j], _A[i]

# Error-proof interface to call "permute"
def permutations(A: List) -> List:
    res = []
    permute(A, 0, res)
    return res

def copy_coords(coords):
    return [coords[0], coords[1]]

def shortest_path(cities: list) -> tuple[list, float]:
    # All possible paths
    possibilities = permutations(cities)
    shortest = None
    for path in possibilities:
        total_dist = 0
        _path = [copy_coords(i) for i in path]
        # Sum distance of every pair of neighbour cities
        while len(_path) > 1:
            total_dist += dist(_path[0], _path[1])
            _path.pop(0)
        # Distance from final city to starting city
        total_dist += dist(path[0], path[-1])
        if shortest is None:
            shortest = (total_dist, path)
        elif total_dist < shortest[0]:
            shortest = (total_dist, path)
    return shortest


if __name__ == "__main__":
    import random

    path = [[random.randrange(-50, 50), random.randrange(-50, 50)] for _ in range(10)]
    print(f"Looking for shortest path for cities {path}")
    total_dist, path = shortest_path(path)
    print(total_dist, path)
