#!/usr/bin/python3
import unittest
from models.state import State
import datetime


class TestState(unittest.TestCase):
    """ Test for state file """

    def test_types(self):
        """Test for attribute type.
        """
        state = State()
        self.assertIsInstance(state.id, str)
        self.assertEqual(type(state.id), str)
        self.assertIsInstance(state.created_at, datetime.datetime)
        self.assertIsInstance(state.updated_at, datetime.datetime)
        self.assertIsInstance(state.name, str)

    def test_has_attributes(self):
        """Test if defined attributes are present.
        """
        state = State()
        self.assertTrue(hasattr(state, 'id'))
        self.assertTrue(hasattr(state, 'created_at'))
        self.assertTrue(hasattr(state, 'updated_at'))
        self.assertTrue(hasattr(state, 'name'))


if __name__ == '__main__':
    unittest.main()
