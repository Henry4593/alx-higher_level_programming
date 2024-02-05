#!/usr/bin/python3
"""Retrieves a list of an object's available attributes.

This function provides a convenient way to explore the attributes and methods
that can be accessed on a given object, including both those defined directly
on the object itself and those inherited from its classes and superclasses.

Args:
    obj: The object whose attributes you want to list.

Returns:
    A list of strings, each representing an attribute name available on the
    object. Note that this list may include special methods (e.g., those
    surrounded by double underscores), class-level attributes, and inherited
    attributes.

Examples:
    # List attributes of a string object:
    >>> lookup("Mary")
    ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', ... ]

    # List attributes of a custom class instance:
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
    >>> person = Person("Mary", 18)
    >>> lookup(person)
    ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', ... ,
    'age', 'name']
"""


def lookup(obj):
    """Returns a list of an object's available attributes.

    This function calls the built-in `dir()` function to retrieve the
    attributes and methods of the object, providing a convenient way to
    explore its accessible properties.
    """

    return dir(obj)
