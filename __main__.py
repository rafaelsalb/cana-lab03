from subsets import zero_sum
from traveling_salesman import shortest_path


def main():
    print("Exercicio 3 - Soma de subconjuntos")
    print(zero_sum([-2, -1, 0, 1, 2]))
    print("Exercicio 4 - Caixeiro-viajante")
    path = [
        [0, 0],
        [1, 1],
        [1, 0],
        [1, 5],
        [2, 3],
        [4, -2],
        [-15, 3],
        [3, 2],
        [-2, 4],
        [5, -2]
    ]
    total_dist, _shortest_path = shortest_path(path)
    print(total_dist, _shortest_path)



if __name__ == "__main__":
    main()
