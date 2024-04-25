#!/usr/bin/python3
"""This module provides a function to find a peak in a list of unsorted
integers.

A peak is defined as an element that is greater than its neighbors. The
function returns the value of the peak element, or None if the list is empty
or has no peak (e.g., a constantly increasing or decreasing list).
"""


def find_peak(list_of_integers):
    """Finds a peak element in a list of unsorted integers.

    Args:
        list_of_integers: A list of integers.

    Returns:
        The value of a peak element in the list, or None if no peak is found.
    """
    lint = list_of_integers
    if lint:
        lint.sort()
        return lint[-1]
    else:
        return None
