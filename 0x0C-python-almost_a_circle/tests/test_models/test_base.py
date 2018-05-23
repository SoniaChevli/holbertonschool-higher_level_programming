#!/usr/bin/python3
"""
Unittest for base.py
"""
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """ Tests for base"""
    def test_base_parameters(self):
        """ what if the id is empty"""
        b = Base(1)
        self.assertIsNotNone(id(b))

    def test_instance(self):
        b = Base(10)
        self.assertIsInstance(b, Base)

    def test_to_json_string(self):
        """ json to string """
        b = Base(32)
        self.assertEqual(b.to_json_string([]), '[]')
        self.assertEqual(b.to_json_string(None), '[]')
        dict = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        d2 = b.to_json_string(dict)
        self.assertTrue(type(d2) is str)
        self.assertTrue(len(d2) > 0)

    def test_from_json(self):
        """ from json """
        b = Base(50)
        self.assertEqual(b.from_json_string('[]'), [])
        self.assertEqual(b.from_json_string(None), [])
