#!/usr/bin/python3
"""Module for efficient matrix multiplication using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Efficiently multiplies two matrices using NumPy's optimized functions.

    Args:
        m_a (list of lists): The first matrix, represented as
                              a list of lists of numbers.
        m_b (list of lists): The second matrix, represented as
                              a list of lists of numbers.

    Returns:
        numpy.ndarray: A NumPy array representing the product of m_a and m_b.

    Raises:
        ValueError: If the matrices have incompatible
                     dimensions for multiplication.
    """
    return (np.matmul(m_a, m_b))
