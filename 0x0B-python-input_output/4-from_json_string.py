#!/usr/bin/python3

"""Offers a function for converting JSON strings to Python objects."""

import json


def from_json_string(my_str):
    """Transforms a JSON string into its corresponding Python object.

    Args:
        my_str (str): The JSON string to be converted.

    Returns:
        The Python object represented by the JSON string.

    Raises:
        ValueError: If the input string is not valid JSON.
    """

    return json.loads(my_str)
