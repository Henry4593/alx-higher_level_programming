#!/usr/bin/python3
"""Functions for modifying text files."""


def append_after(filename="", search_string="", new_string=""):
    """Strategically inserts text within a file.

    Appends the provided new_string after each line in the specified file
    that contains the given search_string.

    Args:
       filename (str): The name of the file to be modified.
       search_string (str): The string to locate within the file.
       new_string (str): The string to be added.
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
