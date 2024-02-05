#!/usr/bin/python3
"""
Extends the built-in list class with a method for printing elements in
sorted order.

This module defines a custom class called `MyList` that inherits from the
standard Python `list` class. It adds a single method, `print_sorted()`, which
allows you to conveniently print the elements of a `MyList` object in sorted
ascending order.

This can be useful when you need to display a list's contents in a specific
order without modifying the underlying list itself.
"""


class MyList(list):
    """
    A list class that extends the built-in list with a sorted printing method.

    Inherits all the functionality of the standard `list` class and adds the
    `print_sorted()` method for printing elements in sorted order.
    """

    def print_sorted(self):
        """
        Prints the elements of the list in sorted ascending order.

        Does not modify the original list itself.
        """
        print(sorted(self))
