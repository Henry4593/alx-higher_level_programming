#!/usr/bin/python3
"""Module for adding integers."""


def add_integer(a, b=98):
    """Adds two integers together.

    Args:
       a: The first integer to add. Must be an integer or a float.
       b: The second integer to add. Defaults to 98.
          Must be an integer or a float.

   Raises:
       TypeError: If either 'a' or 'b' is not an integer or a float.

   Returns:
       The sum of the two integers as an integer.

   """

    if not a or (type(a) != int and type(a) != float):
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
