#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represents a square with a given size.

    Attributes:
        __size: The length of one side of the square.
    """

    def __init__(self, size):
        """Initializes a new Square object.

        Args:
            size: The size of the square's side. Must be a positive integer.
        """

        self.__size = size
