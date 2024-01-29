#!/usr/bin/python3
"""Module for finding the maximum integer in a list."""


def max_integer(list=[]):
    """Finds and returns the maximum integer in a list of integers.

    Args:
        list (list): A list of integers. Defaults to an empty list.

    Returns:
        int: The maximum integer in the list, or None if the list is empty.
    """

    if not list:  # Check for empty list efficiently
        return None

    max_int = list[0]  # Initialize maximum with the first element
    for num in list[1:]:  # Iterate through remaining elements
        if num > max_int:
            max_int = num

    return max_int
