#!/usr/bin/python3
"""Provides a function to convert Python classes to JSON-like dictionaries."""


def class_to_json(obj):
    """Converts a class instance to a dictionary representation.

    This function extracts the instance's attributes and their values,
    creating a dictionary that mirrors the object's structure.

    Args:
        obj: The class instance to be converted.

    Returns:
        A dictionary representing the object's attributes and values.
    """

    return obj.__dict__
