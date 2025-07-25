#!/usr/bin/python3

"""Solves the N-queens puzzle."""


import sys


def init_board(n):
    """
    Initializes an empty N×N chessboard.

    Args:
        n (int): The size of the board.

    Returns:
        list: A 2D list representing the empty chessboard.
    """
    board = []
    [board.append([]) for _ in range(n)]
    [row.append(' ') for _ in range(n) for row in board]
    return (board)


def board_deepcopy(board):
    """
    Creates a deep copy of a chessboard.

    Args:
        board (list): The chessboard to copy.

    Returns:
        list: A deep copy of the input board.
    """
    if isinstance(board, list):
        return list(map(board_deepcopy, board))
    return (board)


def get_solution(board):
    """
    Converts a solved board into the required output format.

    Args:
        board (list): The current chessboard.

    Returns:
        list: A list of [row, column] positions of the queens.
    """
    solution = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == "Q":
                solution.append([r, c])
                break
    return (solution)


def xout(board, row, col):
    """
    Marks all cells that are attacked by a queen placed at (row, col).

    Args:
        board (list): The current chessboard.
        row (int): The row of the queen.
        col (int): The column of the queen.
    """
    for c in range(col + 1, len(board)):
        board[row][c] = "x"
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"
    for r in range(row + 1, len(board)):
        board[r][col] = "x"
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"
    c = col + 1
    for r in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    c = col - 1
    for r in range(row + 1, len(board)):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1


def recursive_solve(board, row, queens, solutions):
    """
    Uses recursion and backtracking to find all N-Queens solutions.

    Args:
        board (list): The current state of the chessboard.
        row (int): The current row to place a queen.
        queens (int): The current number of placed queens.
        solutions (list): A list of valid solutions found so far.

    Returns:
        list: The list of all valid solutions.
    """
    if queens == len(board):
        solutions.append(get_solution(board))
        return (solutions)

    for c in range(len(board)):
        if board[row][c] == " ":
            tmp_board = board_deepcopy(board)
            tmp_board[row][c] = "Q"
            xout(tmp_board, row, c)
            solutions = recursive_solve(tmp_board, row + 1,
                                        queens + 1, solutions)

    return (solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)
    n = int(sys.argv[1])
    board = init_board(n)
    solutions = recursive_solve(board, 0, 0, [])
    for sol in solutions:
        print(sol)
