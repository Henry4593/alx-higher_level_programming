#!/usr/bin/python3
"""Defines an inherited class-checking function."""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.

    Returns:
        bool: True if obj is an inherited instance of a_class, False otherwise.

    Raises:
        TypeError: If obj is not an object or a_class is not a type.

    Example:
       >>> class Parent:
       ...     pass
       ...
       >>> class Child(Parent):
       ...     pass
       ...
       >>> child = Child()
       >>> inherits_from(child, Parent)
       True
       >>> inherits_from(child, Child)
       False
       >>> inherits_from(child, str)
       False
    """

    if not isinstance(obj, object):
        raise TypeError("obj must be an object")
    if not isinstance(a_class, type):
        raise TypeError("a_class must be a type")

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
