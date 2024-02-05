#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle using BaseGeometry.

    Inherits from BaseGeometry to provide basic geometric functionality.
    """

    def __init__(self, width, height):
        """Initializes a new Rectangle.

        Args:
            width (int): The width of the rectangle. Must be an integer
                         greater than 0.
            height (int): The height of the rectangle. Must be an integer
                          greater than 0.

        Raises:
            ValueError: If either width or height is not a positive integer.
        """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
