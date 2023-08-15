#!/usr/bin/python3
"""Module for testing Place"""
import unittest
import pep8
from models.place import Place

class Place_testing(unittest.TestCase):
    """Class to check BaseModel"""

    def testpep8(self):
        """Method for testing codestyle"""
        pepstylecode = pep8.StyleGuide(quiet=True)
        path_user = 'models/place.py'
        result = pepstylecode.check_files([path_user])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
