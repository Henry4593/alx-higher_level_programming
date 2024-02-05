#!/usr/bin/python3
"""Creates a Square class as a specialized version of the Rectangle class."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Models a square, which is a rectangle with all sides equal in length."""

    def __init__(self, size):
        """Sets up a new square instance.

        Args:
            size (int): Specifies the length of each side of the square.
        """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self) -> str:
        """Provides a formatted string representation of the square.

        Returns:
            str: A string that includes the class name (Square) and the
                 size of the square.
        """

        return '[Square] ' + str(self.__size) + '/' + str(self.__size)
