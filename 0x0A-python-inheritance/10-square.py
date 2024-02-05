#!/usr/bin/python3
"""Creates a Square class that extends the Rectangle class."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square, a shape with four equal sides."""

    def __init__(self, size):
        """Establishes a new square instance.

        Args:
            size (int): The length of each side of the square.
        """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
