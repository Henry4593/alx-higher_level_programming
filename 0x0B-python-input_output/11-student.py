#!/usr/bin/python3
"""Defines a class to model a student with their personal details."""


class Student:
    """Encapsulates the information of a student."""

    def __init__(self, first_name, last_name, age):
        """Creates a new Student instance.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Generates a dictionary representation of the student's data.

        Optionally allows specifying which attributes to include.

        Args:
            attrs (list, optional): A list of attribute names to include.
                Defaults to all attributes.

        Returns:
            dict: A dictionary containing the selected student attributes.
        """
        if (type(attrs) == list and
                all(type(element) == str for element in attrs)):
            return ({key: getattr(self, key)
                     for key in attrs if hasattr(self, key)})
        return self.__dict__

    def reload_from_json(self, json):
        """Updates the student's attributes based on the given dictionary.

        Args:
            json (dict): A dictionary containing key-value pairs to update.
        """
        for key, value in json.items():
            setattr(self, key, value)
