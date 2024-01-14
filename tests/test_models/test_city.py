#!/usr/bin/python3
"""Unittest module for the City Class."""

import unittest
from datetime import datetime
import time
from models.city import City
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestCity(unittest.TestCase):

    """Test Cases for the City class."""

    def setUp(self):
        """Sets up test methods."""
        pass

    def tearDown(self):
        """Tears down test methods."""
        self.resetStorage()
        pass

    def reset_Storage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_instant(self):
        """Tests instantiation of City class."""
        X = City()
        self.assertEqual(str(type(X)), "<class 'models.city.City'>")
        self.assertIsInstance(X, City)
        self.assertTrue(issubclass(type(X), BaseModel))

    def test_name_is_public_class_attribute(self):
        my_city = City()
        self.assertEqual(str, type(City.name))
        self.assertIn("name", dir(my_city))
        self.assertNotIn("name", my_city.__dict__)

    def test_attrs(self):
        """Tests the attributes of City class"""
        attributes = storage.attributes()["City"]
        citY = City()
        for k, v in attributes.items():
            self.assertTrue(hasattr(citY, k))
            self.assertEqual(type(getattr(citY, k, None)), v)


if __name__ == "__main__":
    unittest.main()
