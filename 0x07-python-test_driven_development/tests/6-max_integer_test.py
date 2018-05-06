#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Tests for 6-max_integer.py"""

    def setUp(self):
        pass

    def test_10_is_max(self):
        """is 10 the max integer?"""
        self.assertEqual(max_integer([1, 2, 3, 10]), 10)

    def test_len_0(self):
        """is the length of matrix 0"""
        self.assertEqual(max_integer([]), None)

    def test_negative(self):
        """how it reacts to negative numbers"""
        self.assertEqual(max_integer([3, -2, -1, -100]), 3)

    def test_not_matrix(self):
        """no matrix given"""
        self.assertEqual(max_integer([3]), 3)

    def test_double_matrix(self):
        """ given double matrix"""
        self.assertEqual(max_integer([[2, 3], [2, 4]]), [2, 4])

    def test_matrix_letters(self):
        """ only letters in matrix """
        self.assertEqual(max_integer(["A", "B", "C"]), 'C')


if __name__ == '__main__':
    unittest.main()
