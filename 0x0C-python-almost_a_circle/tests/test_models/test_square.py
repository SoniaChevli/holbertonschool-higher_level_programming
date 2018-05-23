#!/usr/bin/python3
""" unittest for square"""
import unittest
import sys

from models.square import Square


class TestSquare(unittest.TestCase):
    ''' tests for squaer.py'''
    def setUp(self):
        '''unitest setup'''
        pass

    def test_init(self):
        """ check if instance works """
        s = Square(10)
        self.assertIsInstance(s, Square)

    def test_id(self):
        """ check if initalized to None"""
        s = Square(5)
        self.assertIsNotNone(id(s))

    def test__gettersetter(self):
        """ checks if the values getter adn setter work"""
        s = Square(9, 7, 8)
        self.assertEqual(s.size, 9)
        self.assertEqual(s.x, 7)
        self.assertEqual(s.y, 8)
    

    def test_xy_0(self):
        """ check no value passed to x and y"""
        s = Square(9)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_error_messages(self):
        """
        wrong values passed
        """
        s = Square(1)
        with self.assertRaisesRegexp(ValueError, "width must be > 0"):
            s.width = -1
        with self.assertRaisesRegexp(ValueError, 'height must be > 0'):
            s.height = -9
        with self.assertRaisesRegexp(ValueError, "width must be > 0"):
            s.width = 0
        with self.assertRaisesRegexp(ValueError, 'height must be > 0'):
            s.height = 0
        with self.assertRaisesRegexp(TypeError, "width must be an integer"):
            s.width = 'sonia'
        with self.assertRaisesRegexp(TypeError, "height must be an integer"):
            s.height = 'sonia'
        with self.assertRaisesRegexp(ValueError, 'x must be >= 0'):
            s.x = -1
        with self.assertRaisesRegexp(ValueError, 'y must be >= 0'):
            s.y = -9

    def test_str(self):
        """ check str was returned corectly"""
        s = Square(4, 1, 2, 3)
        self.assertEqual(str(s), '[Square] (3) 1/2 - 4')

    def test__gettersetter(self):
        """ checks if the values getter adn setter work"""
        s = Square(9, 8, 5)
        self.assertEqual(s.size, 9)
        self.assertEqual(s.x, 8)
        self.assertEqual(s.y, 5)

    def test_xy_0(self):
        """ check no value passed to x and y"""
        s = Square(9)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_update(self):
        """ check updates values correctly"""
        s = Square(3)
        s.update(10, 10, 10, 10)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.x, 10)
        self.assertEqual(s.y, 10)

    def test_update_kwargs(self):
        """ check how kwargs affects update"""
        s = Square(3)
        s.update(size = 24)
        self.assertEqual(s.size, 24)
        s.update(x = 23)
        self.assertEqual(s.x, 23)
        s.update(y = 45)
        self.assertEqual(s.y, 45)
        s.update(10, 10, 10, 10, y=4, x=4, size=34)
        self.assertEqual(s.y, 10)
        self.assertEqual(s.x, 10)
        self.assertEqual(s.size, 10)

    def test_dictionary(self):
        """ check returns correct dictionary representation """
        s = Square(10, 2, 1, 1)
        s_dict = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        s2_dict = s.to_dictionary()
        self.assertEqual(s2_dict, s_dict) 


    @classmethod
    def teardownClass(cls):
        """ removes tests"""
        pass
