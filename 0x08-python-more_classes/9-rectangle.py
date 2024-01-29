#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represents a rectangle with a width and height.

    Attributes:
        number_of_instances (int): The number of Rectangle instances created.
        print_symbol (str): The symbol used to represent the rectangle when
                            printed.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle instance.

        Args:
            width (int): The width of the rectangle. Defaults to 0.
            height (int): The height of the rectangle. Defaults to 0.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is negative.
        """

        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle.

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
        """Gets the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle.

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
        """Calculates and returns the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates and returns the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares two rectangles and returns the one with the greater area.

        Args:
            rect_1 (Rectangle): The first rectangle.
            rect_2 (Rectangle): The second rectangle.

        Raises:
            TypeError: If either rect_1 or rect_2 is not a Rectangle instance.

        Returns:
            Rectangle: The rectangle with the greater area.
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Creates a new Rectangle instance with equal width and height.

        Args:
            size (int): The width and height of the square. Defaults to 0.

        Returns:
            Rectangle: The new square Rectangle instance.
        """

        return cls(size, size)

    def __str__(self):
        """Returns a printable representation of the rectangle using
           # characters.

        Returns:
            str: A string of # characters representing the rectangle's shape.
                  If width or height is 0, returns an empty string.
        """

        if self.__width == 0 or self.__height == 0:
            return ""

        created_rect = []
        for idx_i in range(self.__height):
            [created_rect.append(str(self.print_symbol)) for idx_j in range(self.__width)]
            if idx_i != self.__height - 1:
                created_rect.append("\n")
        return "".join(created_rect)

    def __repr__(self):
        """Returns a string representation of the rectangle for unambiguous
           identification.

        Returns:
            str: A string in the format "Rectangle(width, height)".
        """

        created_rect = "Rectangle(" + str(self.__width)
        created_rect += ", " + str(self.__height) + ")"
        return (created_rect)

    def __del__(self):
        """Prints a message when a Rectangle instance is deleted."""

        type(self).number_of_instances -= 1
        print("Bye rectangle...")
