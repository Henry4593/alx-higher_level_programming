#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represents a square with a given side length.

    Attributes:
        __size (int): The length of one side of the square (private).
    """

    def __init__(self, size=0):
        """Initializes a new Square object with the given size.

        Args:
            size (int, optional): The initial size of the square's side.
                                  Defaults to 0.
        """

        self.size = size

    @property
    def size(self):
        """Gets the current size of the square."""

        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square, ensuring it's a non-negative integer.

        Args:
            value (int): The new size to set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is negative.
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self) -> int:
        """Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """

        return self.__size * self.__size
