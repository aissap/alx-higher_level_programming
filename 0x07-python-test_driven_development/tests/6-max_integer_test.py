#!/usr/bin/python3

"""Unittests for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def test_positive_numbers(self):
        numbers = [1, 2, 3, 4, 5]
        result = max_integer(numbers)
        self.assertEqual(result, 5)

    def test_negative_numbers(self):
        numbers = [-1, -2, -3, -4, -5]
        result = max_integer(numbers)
        self.assertEqual(result, -1)

    def test_mixed_numbers(self):
        numbers = [1, -2, 3, -4, 5]
        result = max_integer(numbers)
        self.assertEqual(result, 5)

    def test_empty_list(self):
        numbers = []
        result = max_integer(numbers)
        self.assertIsNone(result)

    def test_one_element_list(self):
        numbers = [7]
        result = max_integer(numbers)
        self.assertEqual(result, 7)

    def test_float_numbers(self):
        numbers = [1.1, 2.2, 3.3, 4.4]
        result = max_integer(numbers)
        self.assertEqual(result, 4.4)

    def test_empty_string(self):
        result = max_integer("")
        self.assertIsNone(result)

    def test_string(self):
        result = max_integer("hello")
        self.assertEqual(result, 'o')

    def test_list_of_strings(self):
        strings = ["apple", "banana", "cherry"]
        result = max_integer(strings)
        self.assertEqual(result, 'cherry')

    def test_special_characters(self):
        characters = ['!', '@', '#', '$', '%']
        result = max_integer(characters)
        self.assertEqual(result, '%')

if __name__ == '__main__':
    unittest.main()
