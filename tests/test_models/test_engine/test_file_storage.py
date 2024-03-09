#!/usr/bin/python3

"""
Unittest for FileStorage class
"""

import unittest
import os
import json
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.file_storage = FileStorage()

    def tearDown(self):
        del self.file_storage
        self.remove_file_if_exists("file.json")

    def test_all_method(self):
        objects_dict = self.file_storage.all()
        self.assertIsInstance(objects_dict, dict)
        self.assertEqual(objects_dict, self.file_storage._FileStorage__objects)

    def test_new_method(self):
        new_object = BaseModel()
        self.file_storage.new(new_object)
        key = f"{new_object.__class__.__name__}.{new_object.id}"
        self.assertIn(key, self.file_storage._FileStorage__objects)
        self.assertEqual(
            self.file_storage._FileStorage__objects[key], new_object
        )

    def test_save_and_retrive_methods(self):
        # Create & save objects
        obj1 = BaseModel()
        obj2 = User()
        obj3 = State()
        self.file_storage.new(obj1)
        self.file_storage.new(obj2)
        self.file_storage.new(obj3)
        self.file_storage.save()

        # Check if file is created
        self.assertTrue(os.path.exists("file.json"))

    def remove_file_if_exists(self, filename):
        try:
            os.remove(filename)
        except FileNotFoundError:
            pass


if __name__ == '__main__':
    unittest.main()
