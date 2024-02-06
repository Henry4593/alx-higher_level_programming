#!/usr/bin/python3
"""Provides a function for appending text to UTF-8 files."""


def append_write(filename="", text=""):
    """Adds text to the end of an existing UTF-8 text file.

    Args:
        filename (str): The file to receive the appended text.
        text (str): The content to be added to the file.

    Returns:
        int: The count of characters successfully appended.

    Raises:
        OSError: If an error occurs while opening or writing to the file.
    """

    with open(filename, "a", encoding="utf-8") as file_append:
        return file_append.write(text)
