from typing import List
coords = list[int, int]

# distância euclidiana
def dist(A: coords, B: coords) -> float:
    return ((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2) ** (1/2)

# gera todas as permutações da coleção
def permute(A, i, res):
    _A = [i for i in A]
    n = len(_A)
    if i == n:
        res.append(_A)
    for j in range(i, n):
        _A[i], _A[j] = _A[j], _A[i]
        permute(_A, i + 1, res)
        _A[i], _A[j] = _A[j], _A[i]

# interface à prova de erros para a função "permute"
def permutations(A: List) -> List:
    res = []
    permute(A, 0, res)
    return res

def copy_coords(coords):
    return [coords[0], coords[1]]

def shortest_path(cities: list) -> tuple[list, float]:
    # todos os caminhos possíveis
    possibilities = permutations(cities)
    shortest = None
    for path in possibilities:
        total_dist = 0
        _path = [copy_coords(i) for i in path]
        # somando a distância entre cada par de cidades vizinhas
        while len(_path) > 1:
            total_dist += dist(_path[0], _path[1])
            _path.pop(0)
        # distancia da última cidade para a primeira cidade
        total_dist += dist(path[0], path[-1])
        if shortest is None:
            shortest = (total_dist, path)
        elif total_dist < shortest[0]:
            shortest = (total_dist, path)
    return shortest

def greedy_shortest_path(cities: list) -> tuple[list, float]:
    possibilities = [copy_coords(city) for city in cities]
    # escolhe o ponto de partida
    path = [possibilities.pop(0)]
    while len(possibilities) > 0:
        # encontrar cidade mais próxima
        closest_city = 0
        for i in range(1, len(possibilities)):
            if dist(path[-1], possibilities[i]) < dist(path[-1], possibilities[closest_city]):
                closest_city = i
        path.append(possibilities.pop(closest_city))
    total_dist = 0
    for i in range(len(path)):
        total_dist += dist(path[i - 1], path[i])
    return (total_dist, path)


if __name__ == "__main__":
    import random

    path = [[random.randrange(-50, 50), random.randrange(-50, 50)] for _ in range(10)]
    print(f"Caminho: {path}")

    print(f"Procurando o caminho mais curto usando algoritmo guloso:")
    total_dist, path = greedy_shortest_path(path)
    print(total_dist, path)

    print(f"Procurando o caminho mais curto usando força bruta:")
    total_dist, path = shortest_path(path)
    print(total_dist, path)
