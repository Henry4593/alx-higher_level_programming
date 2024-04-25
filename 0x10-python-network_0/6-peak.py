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
    if list_of_integers is None or list_of_integers == []:
        return None
    lo = 0
    hi = len(list_of_integers)
    mid = ((hi - lo) // 2) + lo
    mid = int(mid)
    if hi == 1:
        return list_of_integers[0]
    if hi == 2:
        return max(list_of_integers)
    if list_of_integers[mid] >= list_of_integers[mid - 1] and\
            list_of_integers[mid] >= list_of_integers[mid + 1]:
        return list_of_integers[mid]
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid + 1]:
        return find_peak(list_of_integers[mid:])
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
