#!/usr/bin/python3
"""Provides a function for saving objects to JSON files."""

import json


def save_to_json_file(my_obj, filename):
    """Efficiently writes an object's JSON representation to a text file.

    Args:
        my_obj: The object to be stored as JSON data.
        filename (str): The name of the file to create or overwrite.

    Raises:
        IOError: If an error occurs while writing to the file.
    """

    with open(filename, "w") as file:
        json.dump(my_obj, file)
