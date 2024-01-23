#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represents a square with a given side length and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new Square object.

        Args:
            size (int, optional): The initial size of the square's side.
                                  Defaults to 0.
            position (tuple, optional): The initial position of the square
                                        as (x, y) coordinates.
                                        Defaults to (0, 0).

        Raises:
            TypeError: If size is not an integer or position is not
                       a tuple of two positive integers.
            ValueError: If size is negative.
        """

        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Gets/sets the current position of the square."""

        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square, ensuring it's a tuple of
           two positive integers.

        Args:
            value (tuple): The new position to set, in the format (x, y).

        Raises:
            TypeError: If value is not a tuple of two positive integers.
        """

        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self) -> int:
        """Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """

        return self.__size * self.__size

    def my_print(self):
        """Prints a visual representation of the square
           using the '#' character.
        """

        if self.__size == 0:
            print("")
            return

        [print("") for idx_i in range(0, self.__position[1])]
        for idx_i in range(0, self.__size):
            [print(" ", end="") for idx_j in range(0, self.__position[0])]
            [print("#", end="") for idx_k in range(0, self.__size)]
            print("")
