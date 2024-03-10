#!/usr/bin/python3
import unittest
from models.city import City
import datetime


class TestCity(unittest.TestCase):
    """ Trst for city file """

    def test_types(self):
        """Test for attribute type.
        """
        city = City()
        self.assertIsInstance(city.id, str)
        self.assertEqual(type(city.id), str)
        self.assertIsInstance(city.created_at, datetime.datetime)
        self.assertIsInstance(city.updated_at, datetime.datetime)
        self.assertIsInstance(city.name, str)
        self.assertIsInstance(city.state_id, str)

    def test_has_attributes(self):
        """Test if defined attributes are present.
        """
        city = City()
        self.assertTrue(hasattr(city, 'id'))
        self.assertTrue(hasattr(city, 'created_at'))
        self.assertTrue(hasattr(city, 'updated_at'))
        self.assertTrue(hasattr(city, 'name'))
        self.assertTrue(hasattr(city, 'state_id'))


if __name__ == '__main__':
    unittest.main()
