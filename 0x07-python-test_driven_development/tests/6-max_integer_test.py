#!/usr/bin/python3
"""Unittests for max_integer([..]).

   This module contains unittests for the `max_integer` function, designed to
   verify its correctness for various input scenarios.
"""


import unittest

# Import the max_integer function from the external module '6-max_integer'
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def test_ordered_list(self):
        """Test an ordered list of integers where the
            maximum value is at the end.

            This test ensures that the `max_integer` function correctly
            identifies the maximum value (8) in an ordered list of integers
            where the maximum value is located at the end of the list.
        """
        ordered = [5, 6, 7, 8]
        self.assertEqual(max_integer(ordered), 8)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        unordered = [4, 8, 2, 5]
        self.assertEqual(max_integer(unordered), 8)

    def test_max_at_begginning(self):
        """Test a list with a beginning max value."""
        max_at_beginning = [10, 9, 8, 7]
        self.assertEqual(max_integer(max_at_beginning), 10)

    def test_empty_list(self):
        """Test an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element_list(self):
        """Test a list with a single element."""
        single_element = [3]
        self.assertEqual(max_integer(single_element), 3)

    def test_floats(self):
        """Test a list of floats."""
        floats = [1.73, 6.53, -9.193, 17.8, 7.0]
        self.assertEqual(max_integer(floats), 17.8)

    def test_ints_and_floats(self):
        """Test a list of ints and floats."""
        ints_and_floats = [1.73, 14.2, -5, 10, 7]
        self.assertEqual(max_integer(ints_and_floats), 14.2)

    def test_string(self):
        """Test a string."""
        string = "James"
        self.assertEqual(max_integer(string), 's')

    def test_list_of_strings(self):
        """Test a list of strings."""
        strings = ["I", "love", "my", "pet"]
        self.assertEqual(max_integer(strings), "love")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)


if __name__ == '__main__':
    """Run the unittests when executed as a script."""
    unittest.main()
