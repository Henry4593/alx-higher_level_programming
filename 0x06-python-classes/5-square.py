#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represents a square with a given side length."""

    def __init__(self, size):
        """Initializes a new Square object with the given size.

        Args:
            size (int): The initial size of the square's side.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
        """

        self.size = size  # Calls the setter to validate and set the size

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
            TypeError: If value is not an integer.
            ValueError: If value is negative.
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

    def my_print(self):
        """Prints a visual representation of the square using
           the '#' character.
        """

        for i in range(self.__size):
            print("#" * self.__size)

        if self.__size == 0:
            print("")
