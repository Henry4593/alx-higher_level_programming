#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represent a square.

    Attributes:
        size (int): The size of the square.
        position (tuple): The (x, y) coordinates
                          of the square's top-left corner.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square.

        Args:
            size (int): The size of the new square. Defaults to 0.
            position (tuple, optional): The (x, y) coordinates of the square's
                                        top-left corner. Defaults to (0, 0).

        Raises:
            TypeError: If size is not an integer or position is
                       not a tuple of two integers.
            ValueError: If size is negative or any element in position
                        is negative.
        """

        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Get/set the current position of the square.

        Returns:
            tuple: The (x, y) coordinates of the square's top-left corner.
        """

        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square.

        Args:
            value (tuple): The new (x, y) coordinates of the
                           square's top-left corner.

        Raises:
            TypeError: If value is not a tuple of two integers.
            ValueError: If any element in value is negative.
        """

        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):

            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current area of the square.

        Returns:
            int: The area of the square (size * size).
        """

        return self.__size * self.__size

    def my_print(self):
        """Print the square using the # character.

        This method prints the square at the specified position using the
        '#' character. If the size is 0, it prints nothing.
        """

        if self.__size == 0:
            print("")
            return

        [print("") for idx_i in range(0, self.__position[1])]
        for idx_i in range(0, self.__size):
            [print(" ", end="") for idx_a in range(0, self.__position[0])]
            [print("#", end="") for idx_z in range(0, self.__size)]
            print("")

    def __str__(self):
        """Return a string representation of the square.

        This method returns a string representation of the square, similar
        to the output of the `my_print` method.
        """

        if self.__size != 0:
            [print("") for idx_i in range(0, self.__position[1])]
            for idx_i in range(0, self.__size):
                [print(" ", end="") for idx_a in range(0, self.__position[0])]
                [print("#", end="") for idx_z in range(0, self.__size)]
                if idx_i != self.__size - 1:
                    print("")
        return ""
