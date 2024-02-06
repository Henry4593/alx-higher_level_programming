#!/usr/bin/python3
"""Provides a function for converting string objects to JSON format."""

import json


def to_json_string(my_obj):
    """Converts a string object into its corresponding JSON string
        representation.

    Args:
        my_obj (str): The string object to be converted to JSON.

    Returns:
        str: The JSON string representation of the input string object.

    Raises:
        TypeError: If my_obj is not a string object.
    """

    return json.dumps(my_obj)
