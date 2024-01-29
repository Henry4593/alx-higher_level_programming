#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        print_symbol (str): The symbol used to represent
                            the rectangle in string format.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle. Defaults to 0.
            height (int): The height of the new rectangle. Defaults to 0.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is negative.
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the Rectangle.

        Args:
            value (int): The new width.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the Rectangle.

        Args:
            value (int): The new height.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate and return the area of the Rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate and return the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Return a printable representation of
           the rectangle using the specified symbol.

         Creates a visual representation of the rectangle using the
        `print_symbol` to depict its shape, with newlines separating rows.
         If either width or height is 0, returns an empty string.

        Returns:
            str: A string representation of the rectangle using
                 the specified symbol.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        created_rect = []
        for idx_i in range(self.__height):
            [created_rect.append(str(self.print_symbol))
             for idx_j in range(self.__width)]
            if idx_i != self.__height - 1:
                created_rect.append("\n")
        return "".join(created_rect)

    def __repr__(self):
        """Return a string representation of the rectangle for
           unambiguous recreation.

        Returns:
            str: A string of the form "Rectangle(width, height)", which can be
                 used to recreate a new rectangle with the same dimensions.
        """
        created_rect = "Rectangle(" + str(self.__width)
        created_rect += ", " + str(self.__height) + ")"
        return (created_rect)

    def __del__(self):
        """Print a message when the rectangle is garbage collected.

        Caution: Relying on `__del__` for deterministic resource management is
                 discouraged in Python due to its unpredictable timing and
                 potential to mask exceptions. Consider alternative approaches
                 like context managers or explicit cleanup methods.
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
