from typing import List


def print_board(board):
    for i in board:
        print(i)

def is_safe(board: List, row: int, col: int) -> bool:
    # checa se a linha é segura
    for i in range(col, -1, -1):
        if board[row][i]:
            return False
    
    # checa se a diagonal esquerda-direta é segura
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1

    # checa se a diagonal direita-esquerda é segura
    i = row
    j = col
    while i < 8 and j >= 0:
        if board[i][j]:
            return False
        i += 1
        j -= 1
    
    return True

def eight_queen(board, j, solutions):
    if j >= 8:
        return
    for i in range(8):
        if is_safe(board, i, j):
            board[i][j] = 1
            if j == 7:
                solution = []
                for row in range(8):
                    solution.append([])
                    for col in range(8):
                        solution[row].append(board[row][col])
                solutions.append(solution)
            eight_queen(board, j + 1, solutions)
            board[i][j] = 0


if __name__ == "__main__":
    board = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
    ]
    print_board(board)
    print()
    solutions = []
    eight_queen(board, 0, solutions)
    print(solutions)
    for solution in solutions:
        print_board(solution)
        print()
    print(len(solutions))
    #print_safe_squares(board)
