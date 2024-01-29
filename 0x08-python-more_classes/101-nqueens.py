#!/usr/bin/python3
"""Solves the N-queens puzzle.

   Determines all possible solutions to placing N non-attacking queens
   on an NxN chessboard.

   Example usage:
   $ ./101-nqueens.py N

   Where N is an integer greater than or equal to 4.

   Attributes:
          board (list): A list of lists representing the chessboard.
          solutions (list): A list of lists containing solutions.

   Solutions are represented in the format [[r_queen, c_queen], [r_queen, c_queen], [r_queen, c_queen], [r_queen, c_queen]]
   where `r_queen` and `c_queen` represent the row and column, respectively, where
   a queen must be placed on the chessboard.
"""
import sys


def initialize_board(n):
    """Initialize an n x n sized chessboard with spaces.

    Args:
        n (int): The size of the chessboard.

    Returns:
          list: A list of lists representing the initialized chessboard.
    """
    board = []
    [board.append([]) for idx_i in range(n)]
    [row.append(' ') for idx_i in range(n) for row in board]
    return (board)


def board_deepcopy(board):
    """Return a deepcopy of a chessboard.

    Args:
        board (list): The chessboard to deepcopy.

    Returns:
        list: A deepcopy of the chessboard.
    """
    if isinstance(board, list):
        return list(map(board_deepcopy, board))
    return (board)


def get_solution(board):
    """Return the list of lists representation of a solved chessboard.

       Args:
         board (list): The solved chessboard.

       Returns:
       list: A list of lists containing the positions of the queens.
    """
    solution = []
    for r_queen in range(len(board)):
        for c_queen in range(len(board)):
            if board[r_queen][c_queen] == "Q":
                solution.append([r_queen, c_queen])
                break
    return (solution)


def x_out(board, row, col):
    """X out spots on a chessboard where queens cannot be placed.

    Args:
       board (list): The chessboard to modify.
       row (int): The row where a queen was last placed.
       col (int): The column where a queen was last placed.
    """
    # X out all squares in the same row
    for c_queen in range(col + 1, len(board)):
        board[row][c_queen] = "x"
    for c_queen in range(col - 1, -1, -1):
        board[row][c_queen] = "x"

    # X out all squares in the same column
    for r_queen in range(row + 1, len(board)):
        board[r_queen][col] = "x"
    for r_queen in range(row - 1, -1, -1):
        board[r_queen][col] = "x"

    # X out all squares diagonally down to the right
    c_queen = col + 1
    for r_queen in range(row + 1, len(board)):
        if c_queen >= len(board):
            break
        board[r_queen][c_queen] = "x"
        c_queen += 1

    # X out all squares diagonally up to the left
    c_queen = col - 1
    for r_queen in range(row - 1, -1, -1):
        if c_queen < 0:
            break
        board[r_queen][c_queen] = "x"
        c_queen -= 1

    # X out all squares diagonally up to the right
    c_queen = col + 1
    for r_queen in range(row - 1, -1, -1):
        if c_queen >= len(board):
            break
        board[r_queen][c_queen] = "x"
        c_queen += 1

    # X out all squares diagonally down to the left
    c_queen = col - 1
    for r_queen in range(row + 1, len(board)):
        if c_queen < 0:
            break
        board[r_queen][c_queen] = "x"
        c_queen -= 1

def recursive_solution(board, row, queens, solutions):
    """Recursively solve an N-queens puzzle.

    Args:
        board (list): The current working chessboard.
        row (int): The current working row.
        queens (int): The current number of placed queens.
        solutions (list): A list of lists of solutions.

    Returns:
        list: The updated list of solutions.
    """
    if queens == len(board):
        solutions.append(get_solution(board))
        return (solutions)

    for c_queen in range(len(board)):
        if board[row][c_queen] == " ":
            temp_board = board_deepcopy(board)
            temp_board[row][c_queen] = "Q"
            x_out(temp_board, row, c_queen)
            solutions = recursive_solution(temp_board, row + 1,
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

    board = initialize_board(int(sys.argv[1]))
    solutions = recursive_solution(board, 0, 0, [])
    for solution in solutions:
        print(solution)
