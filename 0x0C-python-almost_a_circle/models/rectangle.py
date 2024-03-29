#!/usr/bin/python3
"""Defines a rectangle class inheriting from Base class."""
from models.base import Base


class Rectangle(Base):
    """Represent a rectangle with width, height, coordinates, and optional id.

    Attributes:
        width (int): The width of the rectangle. Must be a positive integer.
        height (int): The height of the rectangle. Must be a positive integer.
        x (int): The x-coordinate of the bottom-left corner of the rectangle.
                 Must be non-negative integer.
        y (int): The y-coordinate of the bottom-left corner of the rectangle.
                 Must be non-negative integer.
        id (int, optional): The unique identifier of the rectangle. If not
                given, automatically assigned by Base class.

    Raises:
        TypeError: If either width, height, x, or y is not an integer.
        ValueError: If either width or height is not positive, or if x or y
                   is negative.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int, optional): The x-coordinate of the new Rectangle.
                 Defaults to 0.
            y (int, optional): The y-coordinate of the new Rectangle.
                 Defaults to 0.
            id (int, optional): The identity of the new Rectangle.
                 Defaults to None.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.
        Args:
            value (int): The new width of the rectangle.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is not positive.
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """get the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """get the x coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """get the y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the Rectangle."""
        return self.width * self.height

    def display(self):
        """Print the Rectangle using the `#` character."""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """Updates the rectangle with new values.

        Args:
            *args (ints, optional): New values for specific attributes.
            - 1st argument: The new id (optional).
            - 2nd argument: The new width (optional).
            - 3rd argument: The new height (optional).
            - 4th argument: The new x-coordinate (optional).
            - 5th argument: The new y-coordinate (optional).
        **kwargs (dict, optional): New key/value pairs for attributes.
            - 'id': The new ID.
            - 'width': The new width.
            - 'height': The new height.
            - 'x': The new x-coordinate.
            - 'y': The new y-coordinate.

        Raises:
            TypeError: If any value in `args` is not an integer.
            ValueError: If any value in `args` is not positive for width or
                        height, or negative for x or y.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the print() and str() representation of the Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
