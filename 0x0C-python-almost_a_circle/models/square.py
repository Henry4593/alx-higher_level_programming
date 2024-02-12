#!/usr/bin/python3
"""Defines a square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a new Square.

        Args:
            size (int): The size of the new Square.
            x (int, optional): The x coordinate of the new Square.
                               Defaults to 0.
            y (int, optional): The y coordinate of the new Square.
                               Defaults to 0.
            id (int, optional): The identity of the new Square.
                               Defaults to None..
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Gets/sets the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size of the Square, updating both width and height.

        Args:
            value (int): The new size of the Square.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than 0.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates Square attributes from positional or keyword arguments.

        Args:
            *args (ints, optional): Positional arguments to update attributes.
                1st: id
                2nd: size
                3rd: x
                4th: y
            **kwargs (dict, optional): Keyword arguments to update attributes.
                id (int): The new id value.
                size (int): The new size value.
                x (int): The new x-coordinate value.
                y (int): The new y-coordinate value.

        Raises:
            TypeError: If an argument is not of the expected type.
            ValueError: If an argument has an invalid value.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Returns a dictionary representation of the Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Returns a formatted string representation of the Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
