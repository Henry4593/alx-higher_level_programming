#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """
    Represents base geometry.

    This class provides a foundation for defining geometric shapes. It
    includes a method for validating integer parameters and a placeholder
    for the area calculation, which should be implemented in subclasses.
    """

    def area(self):
        """Calculates the area of the geometric shape.

        Raises:
            NotImplementedError: This method is not implemented in the base
              class.
            It should be implemented in subclasses to provide specific
            area calculations.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates a parameter as an integer.

        Args:
           name (str): The name of the parameter.
           value (int): The parameter to validate.

        Raises:
           TypeError: If value is not an integer.
           ValueError: If value is less than or equal to 0.
        """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
