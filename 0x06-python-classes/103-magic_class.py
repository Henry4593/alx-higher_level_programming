#!/usr/bin/python3

"""Define a MagicClass matching exactly a bytecode provided"""

import math


class MagicClass:
    """Represent a circle.

    Attributes:
        radius (float): The radius of the circle.
    """

    def __init__(self, radius=0):
        """Initialize a new MagicClass.

        Args:
            radius (float or int): The radius of the new MagicClass.
                                   Defaults to 0.

        Raises:
            TypeError: If radius is not a number.
        """

        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return the area of the circle.

        Returns:
            float: The area of the circle (pi * radius * radius).
        """

        return math.pi * self.__radius * self.__radius

    def circumference(self):
        """Return the circumference of the circle.

        Returns:
            float: The circumference of the circle (2 * pi * radius).
        """

        return 2 * math.pi * self.__radius
