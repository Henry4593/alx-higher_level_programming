#!/usr/bin/python3
"""Creates a Rectangle class that builds upon the BaseGeometry class."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Models a rectangle using the features of BaseGeometry."""

    def __init__(self, width, height):
        """Sets up a new Rectangle instance.

        Args:
            width (int): Specifies the width of the rectangle.
            height (int): Specifies the height of the rectangle.
        """

        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Calculates and returns the rectangle's area."""

        return self.__width * self.__height

    def __str__(self):
        """Provides a formatted string representation of the rectangle."""

        return '[Rectangle] ' + str(self.__width) + '/' + str(self.__height)
