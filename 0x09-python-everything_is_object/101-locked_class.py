#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """
    Enforce that LockedClass instances only possess the explicitly defined
    attribute first_name, prohibiting dynamic attribute creation.    
    """

    __slots__ = ["first_name"]
