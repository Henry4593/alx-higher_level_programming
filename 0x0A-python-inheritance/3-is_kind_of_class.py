#!/usr/bin/python3
"""Defines a class and inherited class-checking function.

  This module contains a function that checks if an object is an instance
  or an inherited instance of a given class.
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance or inherited instance of a class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.

    Returns:
        bool: True if obj is an instance or inherited instance of a_class,
             False otherwise.
    """

    if isinstance(obj, a_class):
        return True
    return False
