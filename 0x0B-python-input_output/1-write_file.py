#!/usr/bin/python3
"""Provides a function for writing text to a file."""


def write_file(filename="", text=""):
    """Saves the given text content into a UTF-8 encoded text file.

    Args:
        filename (str): The name of the file to create or overwrite.
        text (str): The text to be written into the file.

    Returns:
        int: The number of characters successfully written to the file.
    """

    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
