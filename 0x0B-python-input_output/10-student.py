#!/usr/bin/python3
"""Defines a class to model a student with their personal information."""


class Student:
    """Encapsulates the details of a student, including first name, last name,
        and age.
    """

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
        """Generates a dictionary representation of the Student's attributes.

        Args:
            attrs (list, optional): A list of specific attributes to include.
                                    Defaults to None, including all attributes.

        Returns:
            dict: A dictionary containing the specified student attributes.
        """

        if (type(attrs) == list and
                all(type(element) == str for element in attrs)):
            return ({key: getattr(self, key)
                     for key in attrs if hasattr(self, key)})
        return self.__dict__
