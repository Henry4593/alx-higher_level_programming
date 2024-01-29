#!/usr/bin/python3
"""A module for matrix multiplication"""


def matrix_mul(m_a, m_b):
    """Multiplies two matrices together.

    Args:
        m_a (list of lists): The first matrix, represented
                             as a list of lists of numbers.
        m_b (list of lists): The second matrix, represented
                             as a list of lists of numbers.

    Returns:
        list of lists: A new matrix representing the product of m_a and m_b.

    Raises:
        TypeError: If either m_a or m_b is not a list of lists of numbers.
        ValueError: If either matrix is empty or has incompatible dimensions.
    """
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if not all((isinstance(element, int) or isinstance(element, float))
               for element in [num for row in m_a for num in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(element, int) or isinstance(element, float))
               for element in [num for row in m_b for num in row]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must should be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must should be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    inverted_b = []
    for row_idx in range(len(m_b[0])):
        new_row = []
        for col_idx in range(len(m_b)):
            new_row.append(m_b[col_idx][row_idx])
        inverted_b.append(new_row)

    final_matrix = []
    for row in m_a:
        new_row = []
        for col in inverted_b:
            product = 0
            for idx in range(len(inverted_b[0])):
                product += row[idx] * col[idx]
            new_row.append(product)
        final_matrix.append(new_row)

    return final_matrix
