#!/usr/bin/python3
""" unittest for rectangle"""
import unittest
import sys

from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    ''' tests for rectangle.py '''
    def setUp(self):
        """unitest setup """
        pass

    def test_id(self):
        """ check if initalized to None"""
        r = Rectangle(5, 4)
        self.assertIsNotNone(id(r))


    def test_instance(self):
        """check if rectangle works """
        r = Rectangle(1, 10)
        self.assertIsInstance(r, Rectangle)

    def test__gettersetter(self):
        """ checks if the values getter adn setter work"""
        r = Rectangle(9, 7, 8, 5)
        self.assertEqual(r.width, 9)
        self.assertEqual(r.height, 7)
        self.assertEqual(r.x, 8)
        self.assertEqual(r.y, 5)

    def test_xy_0(self):
        """ check no value passed to x and y"""
        r = Rectangle(9, 4)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)



    def test_error_messages(self):
        """
        wrong values passed
        """
        r = Rectangle(1, 2)

        with self.assertRaisesRegexp(ValueError, "width must be > 0"):
            r.width = -1
        with self.assertRaisesRegexp(ValueError, 'height must be > 0'):
            r.height = -9
        with self.assertRaisesRegexp(ValueError, "width must be > 0"):
            r.width = 0
        with self.assertRaisesRegexp(ValueError, 'height must be > 0'):
            r.height = 0
        with self.assertRaisesRegexp(TypeError, "width must be an integer"):
            r.width = 'sonia'
        with self.assertRaisesRegexp(TypeError, "height must be an integer"):
            r.height = 'sonia'
        with self.assertRaisesRegexp(ValueError, 'x must be >= 0'):
            r.x = -1
        with self.assertRaisesRegexp(ValueError, 'y must be >= 0'):
            r.y = -9

    def test_area(self):
        """ checks if correct area returned"""
        r = Rectangle(10, 5)
        self.assertEqual(r.area(), r.width * r.height)
        """
    def test_display(self):

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        r = Rectangle(3, 4)
        
        self.assertEqual(r.display, '###\n###\n###\n###\n')
        """
    def test_str(self):
        """ check str was returned corectly"""
        r = Rectangle(4, 50, 5 ,4, 6)
        self.assertEqual(str(r), '[Rectangle] (6) 5/4 - 4/50')

    def test_update(self):
        """ check updates values correctly"""
        r = Rectangle(1, 2, 3, 4)
        r.update(10, 10, 10, 10, 10)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)
        self.assertEqual(r.id, 10)

        
    def test_update_kwargs(self):
        """ check how kwargs affects update"""
        r = Rectangle(1, 2, 3, 4)
        r.update(height = 24)
        self.assertEqual(r.height, 24)
        r.update(width = 56)
        self.assertEqual(r.width, 56)
        r.update(x = 23)
        self.assertEqual(r.x, 23)
        r.update(y = 45)
        self.assertEqual(r.y, 45)
        r.update(10, 10, 10, 10, 10, y=4, x=4, height=10, width=54)
        self.assertEqual(r.y, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 10)

    def test_to_dictionary(self):
        r = Rectangle(1, 2, 3, 4, 5)
        a = {'width': 1, 'height': 2, 'x': 3, 'y': 4, 'id': 5}
        self.assertTrue(r.to_dictionary() == a)
        r2 = Rectangle(1, 2)
        b = {'width': 1, 'height': 2, 'x': 0, 'y': 0, 'id': 6}
        self.assertEqual(r2.to_dictionary, b)

if __name__ == '__main__':
    unittest.main()
