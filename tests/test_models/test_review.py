#!/usr/bin/python3

import unittest
from models.review import Review
import datetime


class TestReview(unittest.TestCase):
    """ Class to test review file """

    def test_types(self):
        """Test for attribute type.
        """
        review = Review()
        self.assertIsInstance(review.id, str)
        self.assertEqual(type(review.id), str)
        self.assertIsInstance(review.created_at, datetime.datetime)
        self.assertIsInstance(review.updated_at, datetime.datetime)
        self.assertIsInstance(review.text, str)
        self.assertIsInstance(review.place_id, str)
        self.assertIsInstance(review.user_id, str)

    def test_has_attributes(self):
        """Test if defined attributes are present.
        """
        review = Review()
        self.assertTrue(hasattr(review, 'id'))
        self.assertTrue(hasattr(review, 'created_at'))
        self.assertTrue(hasattr(review, 'updated_at'))
        self.assertTrue(hasattr(review, 'user_id'))
        self.assertTrue(hasattr(review, 'text'))
        self.assertTrue(hasattr(review, 'place_id'))


if __name__ == '__main__':
    unittest.main()
