"""Defines a function to check if an object is an exact instance of a class.

This function takes two arguments:
- `obj`: The object to check.
- `a_class`: The class to compare the type of `obj` to.

It returns `True` if `obj` is an exact instance of `a_class`, and `False`
otherwise.
"""


def is_same_class(obj, a_class):
    """
    Checks if an object is an exact instance of a given class.

    Args:
        obj: The object to check.
        a_class: The class to compare the type of obj to.

    Returns:
        True if obj is an exact instance of a_class, False otherwise.
    """

    if type(obj) == a_class:
        return True
    return False
