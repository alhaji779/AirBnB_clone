#!/usr/bin/python3
import unittest
from models.place import Place
import datetime


class TestPlace(unittest.TestCase):
    """ Test for place file """

    def test_types(self):
        """Test for attribute type.
        """
        place = Place()
        self.assertIsInstance(self.place.name, str)
        self.assertEqual(type(self.place.name), str)
        self.assertIsInstance(self.place.id, str)
        self.assertEqual(type(self.place.id), str)
        self.assertIsInstance(self.place.created_at, datetime.datetime)
        self.assertIsInstance(self.place.updated_at, datetime.datetime)
        self.assertIsInstance(self.place.price_by_night, int)
        self.assertIsInstance(self.place.max_guest, int)
        self.assertIsInstance(self.place.description, str)
        self.assertIsInstance(self.place.number_rooms, int)
        self.assertIsInstance(self.place.number_bathrooms, int)
        self.assertIsInstance(self.place.city_id, str)
        self.assertIsInstance(self.place.user_id, str)
        self.assertIsInstance(self.place.amenity_ids, list)
        self.assertIsInstance(self.place.longitude, float)
        self.assertIsInstance(self.place.latitude, float)

    def test_has_attributes(self):
        """Test if defined attributes are present.
        """
        place = Place()
        self.assertTrue(hasattr(self.place, 'name'))
        self.assertTrue(hasattr(self.place, 'id'))
        self.assertTrue(hasattr(self.place, 'created_at'))
        self.assertTrue(hasattr(self.place, 'updated_at'))
        self.assertTrue(hasattr(self.place, 'city_id'))
        self.assertTrue(hasattr(self.place, 'user_id'))
        self.assertTrue(hasattr(self.place, 'description'))
        self.assertTrue(hasattr(self.place, 'number_rooms'))
        self.assertTrue(hasattr(self.place, 'number_bathrooms'))
        self.assertTrue(hasattr(self.place, 'max_guest'))
        self.assertTrue(hasattr(self.place, 'price_by_night'))
        self.assertTrue(hasattr(self.place, 'latitude'))
        self.assertTrue(hasattr(self.place, 'longitude'))
        self.assertTrue(hasattr(self.place, 'amenity_ids'))


if __name__ == '__main__':
    unittest.main()
