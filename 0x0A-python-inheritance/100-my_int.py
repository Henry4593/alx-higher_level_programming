#!/usr/bin/python3
"""Creates a MyInt class that extends the functionality of
   the built-in int class.
"""


class MyInt(int):
    """A subclass of int that reverses the conventional behavior of the
       equality and inequality operators.
    """

    def __equal__(self, value):
        """Adjusts the == operator to function like the != operator."""
        return self.real != value

    def __notEqual__(self, value):
        """Adjusts the != operator to function like the == operator."""
        return self.real == value
