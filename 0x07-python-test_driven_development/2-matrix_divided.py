#!/usr/bin/python3

"""Module for dividing elements of a matrix."""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a given divisor.

    Args:
         matrix (list): A list of lists representing the matrix.
           Each inner list represents a row of the matrix.
         div (int or float): The divisor to divide each element by.

    Returns:
           list: A new matrix with the same dimensions as the input matrix,
           where each element has been divided by the divisor.

    Raises:
          TypeError:
                   If the input matrix is not a list of lists of numbers.
                   If the rows of the matrix have different lengths.
                   If the divisor is not a number (int or float).
          ZeroDivisionError: If the divisor is 0.
   """

    # Validate input types
    if (not isinstance(matrix, list) or
       not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a list of lists")
    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must contain only numbers")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Validate matrix dimensions
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Perform division and return the result
    return [list(map(lambda x: round(x / div, 2), row)) for row in matrix]
