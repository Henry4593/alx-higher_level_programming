#!/usr/bin/python3

"""Define a class to represent a square."""


class Square:
    """Represent a square.

    Attributes:
        size (int): The size of the square.
    """

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): The size of the new square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
        """

        self.size = size

    @property
    def size(self):
        """Get/set the current size of the square.

        Returns:
            int: The current size of the square.
        """

        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square.

        Returns:
            int: The area of the square (size * size).
        """

        return self.__size * self.__size

    def __eq__(self, other):
        """Define the == comparison to another Square.

        Args:
            other (Square): The other Square to compare to.

        Returns:
            bool: True if the areas of the two squares
                  are equal, False otherwise.
        """

        return self.area() == other.area()

    def __ne__(self, other):
        """Define the != comparison to another Square.

        Args:
            other (Square): The other Square to compare to.

        Returns:
            bool: True if the areas of the two squares
                  are not equal, False otherwise.
        """

        return self.area() != other.area()

    def __lt__(self, other):
        """Define the < comparison to another Square.

        Args:
            other (Square): The other Square to compare to.

        Returns:
            bool: True if the area of this square is less than
                  the area of the other square, False otherwise.
        """

        return self.area() < other.area()

    def __le__(self, other):
        """Define the <= comparison to another Square.

        Args:
            other (Square): The other Square to compare to.

        Returns:
            bool: True if the area of this square is less than or equal
                  to the area of the other square, False otherwise.
        """

        return self.area() <= other.area()

    def __gt__(self, other):
        """Define the > comparison to another Square.

        Args:
            other (Square): The other Square to compare to.

        Returns:
            bool: True if the area of this square is greater
                  than the area of the other square, False otherwise.
        """

        return self.area() > other.area()

    def __ge__(self, other):
        """Define the >= comparison to another Square.

        Args:
            other (Square): The other Square to compare to.

        Returns:
            bool: True if the area of this square is greater than
                  or equal to the area of the other square, False otherwise.
        """

        return self.area() >= other.area()
