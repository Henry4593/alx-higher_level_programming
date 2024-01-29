#!/usr/bin/python3
"""Module for printing squares."""


def print_square(size):
    """Prints a square composed of '#' characters to the console.

    Args:
        size (int): The side length of the square.

    Raises:
          TypeError: If `size` is not an integer.
          ValueError: If `size` is less than 0.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be non-negative")

    for _ in range(size):
        print("#" * size)  # Print a row of '#' characters
