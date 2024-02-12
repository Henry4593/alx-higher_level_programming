#!/usr/bin/python3
"""Represents a rectangle on a 2D plane.

This class inherits from the `Base` class and defines additional attributes
specific to a rectangle: width, height, x-coordinate, and y-coordinate.

Attributes:
    width (int): The width of the rectangle (must be positive).
    height (int): The height of the rectangle (must be positive).
    x (int): The x-coordinate of the rectangle'sqr bottom-left corner
             (must be non-negative).
    y (int): The y-coordinate of the rectangle'sqr bottom-left corner
             (must be non-negative).
    id (int, optional): The unique identifier of the rectangle.

Raises:
    TypeError: If any of the following are not integers: width,height, x, or y
    ValueError: If any of the following are non-positive: width, height, or x.

"""
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a new Rectangle object.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the rectangle's bottom-left
                               corner.Defaults to 0.
            y (int, optional): The y-coordinate of the rectangle's bottom-left
                                corner.Defaults to 0.
            id (int, optional): The unique identifier of the rectangle.
                                Defaults to None.

        Raises:
            TypeError: If any of the following are not integers: width,
                        height, x, or y.
            ValueError: If any of the following are non-positive: width,
                        height, or x.

        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Gets the current width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle, ensuring it's a positive integer.

        Args:
            value (int): The new width to set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not positive.

        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be positive")
        self.__width = value

    @property
    def height(self):
        """Gets the current height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle, ensuring it's a positive integer.

        Args:
            value (int): The new height to set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not positive.

        """
        if type(value) not in [int]:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def x(self):
        """Gets the current x-coordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the x-coordinate of the rectangle, ensuring it's non-negative

        Args:
            value (int): The new x-coordinate to set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is negative.

        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Gets the y-coordinate of the Rectangle (non-negative)."""
        return self.__y

    @y.setter
    def y(self, value):
        """Checks if y is a non-negative integer and sets it."""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculates and returns the area of the Rectangle."""
        return self.__width * self.__height

    def display(self):
        """Prints the Rectangle using '#' characters (if not empty)."""
        print("\n" * self.y,  end="")
        print((" " * self.x + "#" * self.__width + '\n') *
              self.__height, end="")

    def update(self, *args, **kwargs):
        """Updates Rectangle attributes from positional or keyword arguments.

        Args:
            *args (ints, optional): Positional arguments to update attributes.
                1st: id
                2nd: width
                3rd: height
                4th: x
                5th: y
            **kwargs (dict, optional): Keyword arguments to update attributes.
                id (int): The new id value.
                width (int): The new width value.
                height (int): The new height value.
                x (int): The new x-coordinate value.
                y (int): The new y-coordinate value.

        Raises:
            TypeError: If an argument is not of the expected type.
            ValueError: If an argument has an invalid value.
        """
        if not args and not kwargs:
            return
        if args is not None:
            attributes = ["id", "width", "height", "x", "y"]
            for idx_i, idx_j in enumerate(args):
                if idx_i < len(attributes):
                    setattr(self, attributes[idx_i], idx_j)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns a dictionary representation of the Rectangle.

        Returns:
            dict: A dictionary containing the attributes of the Rectangle.
        """
        _map = {}
        for key, value in self.__dict__.items():
            if key.startswith("_"):
                _map[key.split("__")[-1]] = value
            else:
                _map[key] = value
        return _map

    def __str__(self):
        """Returns a formatted string representation of the Rectangle.

        Returns:
            str: A string representing the Rectangle in the format
                "[Rectangle] (id) x/y - width/height".
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
