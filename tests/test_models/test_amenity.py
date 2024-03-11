#!/usr/bin/python3

import unittest
from models.amenity import Amenity
import datetime


class TestAmenity(unittest.TestCase):
    """ Class to test amenity file """

    def test_types(self):
        """Test for attribute type.
        """
        amenity = Amenity()
        self.assertIsInstance(amenity.id, str)
        self.assertEqual(type(amenity.id), str)
        self.assertIsInstance(amenity.created_at, datetime.datetime)
        self.assertIsInstance(amenity.updated_at, datetime.datetime)
        self.assertIsInstance(amenity.name, str)

    def test_has_attributes(self):
        """Test if defined attributes are present.
        """
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'id'))
        self.assertTrue(hasattr(amenity, 'created_at'))
        self.assertTrue(hasattr(amenity, 'updated_at'))
        self.assertTrue(hasattr(amenity, 'name'))


if __name__ == '__main__':
    unittest.main()
