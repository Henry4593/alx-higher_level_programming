#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represents a square with a given side length.

    Attributes:
        __size (int): The length of one side of the square.
    """

    def __init__(self, size=0):
        """Initializes a new Square object.

        Args:
            size (int, optional): The size of the square's side. Defaults to 0.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is negative.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
