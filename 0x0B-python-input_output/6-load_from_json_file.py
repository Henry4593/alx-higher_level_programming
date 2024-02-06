#!/usr/bin/python3
"""Provides a function for loading data from JSON files."""

import json


def load_from_json_file(filename):
    """Retrieves and constructs a Python object from the contents
        of a JSON file.

    Args:
        filename (str): The path to the JSON file to be read.

    Returns:
        The Python object represented by the JSON data in the file.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        JSONDecodeError: If the file content is not valid JSON.
    """

    with open(filename) as file:
        return json.load(file)
