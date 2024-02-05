#!/usr/bin/python3
"""Provides a function for dynamically adding attributes to objects."""


def add_attribute(obj, att, value):
    """Attaches a new attribute to an object, if feasible.

    Args:
        obj (object): The target object for the attribute addition.
        att (str): The name of the attribute to be added.
        value (any): The intended value to be assigned to the attribute.

    Raises:
        TypeError: If the object's structure doesn't support attribute
                   addition.
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
