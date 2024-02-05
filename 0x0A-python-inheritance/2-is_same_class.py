#!/usr/bin/python3

"""Provides a function to determine if an object belongs directly to a
    specific class.
"""


def is_same_class(obj, a_class):
    """
    Determines whether an object is an exact instance of a particular class.

    Args:
        obj: The object to evaluate.
        a_class: The class to compare against.

    Returns:
        True if obj is a direct instance of a_class, False otherwise.
    """

    # Determines whether the object's type precisely matches the given class.
    return type(obj) == a_class
