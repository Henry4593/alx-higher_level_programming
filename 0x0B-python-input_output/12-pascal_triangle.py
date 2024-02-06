#!/usr/bin/python3
"""Constructs Pascal's Triangle, a triangular array of numbers with unique
    properties.
"""


def pascal_triangle(n):
    """Generates Pascal's Triangle of a given size.

    Args:
        n (int): The desired size of the triangle. Must be a positive integer.

    Returns:
        list: A list of lists of integers representing Pascal's Triangle,
              where each inner list represents a row of the triangle.

    Raises:
        ValueError: If n is not a positive integer.
    """

    if n <= 0:
        return []

    triangles = [[1]]

    while len(triangles) != n:
        tri = triangles[-1]
        temp = [1]

        for idx in range(len(tri) - 1):
            temp.append(tri[idx] + tri[idx + 1])

        temp.append(1)
        triangles.append(temp)

    return triangles
