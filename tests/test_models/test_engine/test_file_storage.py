#!/usr/bin/python3
"""Unittest module for the FileStorage class."""

import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import re
import json
import os
import time


class TestFile_Storage(unittest.TestCase):
    """Test Cases for the FileStorage class"""

    def setUp(self):
        """Sets up test methods."""
        pass

    def reset_Storage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def tearDown(self):
        """Tears down test methods."""
        self.resetStorage()
        pass

    def test_instant(self):
        """
        Tests instantiation of storage class
        """
        self.assertEqual(type(storage).__name__, "FileStorage")

    def test_no_args(self):
        """Tests __init__ with no arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            FileStorage.__init__()
        message = "descriptor '__init__' of 'object' object needs an argument"
        self.assertEqual(str(e.exception), message)

    def test_kwargs(self):
        """Tests __init__ with many arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            b = FileStorage(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        m = "object() takes no parameters"
        self.assertEqual(str(e.exception), m)

    def test_attr(self):
        """Tests class attributes."""
        self.resetStorage()
        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))
        self.assertTrue(hasattr(FileStorage, "_FileStorage__objects"))
        self.assertEqual(getattr(FileStorage, "_FileStorage__objects"), {})

    def help_test_all(self, classname):
        """Helper tests all() method for classname."""
        self.resetStorage()
        self.assertEqual(storage.all(), {})
        o = storage.classes()[classname]()
        storage.new(o)
        key = "{}.{}".format(type(o).__name__, o.id)
        self.assertTrue(key in storage.all())
        self.assertEqual(storage.all()[key], o)

    def test_all_base_model(self):
        """Tests all() method for BaseModel."""
        self.help_test_all("BaseModel")

    def test_all_user(self):
        """Tests all() method for User."""
        self.help_test_all("User")

    def test_all_state(self):
        """Tests all() method for State."""
        self.help_test_all("State")

    def test_all_city(self):
        """Tests all() method for City."""
        self.help_test_all("City")

    def test_all_amenity(self):
        """Tests all() method for Amenity."""
        self.help_test_all("Amenity")

    def test_all_place(self):
        """Tests all() method for Place."""
        self.help_test_all("Place")

    def test_all_review(self):
        """Tests all() method for Review."""
        self.help_test_all("Review")

    def test_all_base_model(self):
        """Tests all() method with many objects."""
        self.help_test_all_multiple("BaseModel")

    def test_all_no_args(self):
        """Tests all() with no arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            FileStorage.all()
        msg = "all() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_all_excess_args(self):
        """Tests all() with too many arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            FileStorage.all(self, 98)
        msg = "all() takes 1 positional argument but 2 were given"
        self.assertEqual(str(e.exception), msg)

    def test_new_base_model(self):
        """Tests new() method for BaseModel."""
        self.help_test_new("BaseModel")

    def test_new_user(self):
        """Tests new() method for User."""
        self.help_test_new("User")

    def test_new_state(self):
        """Tests new() method for State."""
        self.help_test_new("State")

    def test_new_city(self):
        """Tests new() method for City."""
        self.help_test_new("City")

    def test_new_amenity(self):
        """Tests new() method for Amenity."""
        self.help_test_new("Amenity")

    def test_new_place(self):
        """Tests new() method for Place."""
        self.help_test_new("Place")

    def test_new_review(self):
        """Tests new() method for Review."""
        self.help_test_new("Review")

    def test_new_no_args(self):
        """Tests new() with no arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            storage.new()
        msg = "missing 1 required positional argument: 'obj'"
        self.assertEqual(str(e.exception), msg)

    def help_test_save(self, classname):
        """Helps tests save() method for classname."""
        self.resetStorage()
        cls = storage.classes()[classname]
        o = cls()
        storage.new(o)
        key = "{}.{}".format(type(o).__name__, o.id)
        storage.save()
        self.assertTrue(os.path.isfile(FileStorage._FileStorage__file_path))
        d = {key: o.to_dict()}
        with open(FileStorage._FileStorage__file_path,
                  "r", encoding="utf-8") as f:
            self.assertEqual(len(f.read()), len(json.dumps(d)))
            f.seek(0)
            self.assertEqual(json.load(f), d)

    def test_save_base_model(self):
        """Tests save() method for BaseModel."""
        self.help_test_save("BaseModel")

    def test_save_user(self):
        """Tests save() method for User."""
        self.help_test_save("User")

    def test_save_state(self):
        """Tests save() method for State."""
        self.help_test_save("State")

    def test_save_city(self):
        """Tests save() method for City."""
        self.help_test_save("City")

    def test_save_amenity(self):
        """Tests save() method for Amenity."""
        self.help_test_save("Amenity")

    def test_save_place(self):
        """Tests save() method for Place."""
        self.help_test_save("Place")

    def test_save_review(self):
        """Tests save() method for Review."""
        self.help_test_save("Review")

    def test_save_no_args(self):
        """Tests save() with no arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            FileStorage.save()
        msg = "save() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_kwargs(self):
        """Tests save() with too many arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            FileStorage.save(self, 98)
        msg = "save() takes 1 positional argument but 2 were given"
        self.assertEqual(str(e.exception), msg)


if __name__ == '__main__':
    unittest.main()
