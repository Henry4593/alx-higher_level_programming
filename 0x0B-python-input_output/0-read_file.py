#!/usr/bin/python3
"""Provides a function for convenient text file reading."""


def read_file(filename=""):
    """Displays the contents of a UTF-8 encoded text file on the console.

        Args:
            filename (str): The name or path of the text file to read.
            If not provided, defaults to reading from standard input (stdin).
    """

    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
