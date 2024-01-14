#!/usr/bin/python3
"""Unittest module for the Amenity Class."""

import unittest
from datetime import datetime
import time
from models.amenity import Amenity
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class Test_Amenity(unittest.TestCase):

    """Test Cases for the Amenity class."""

    def setUp(self):
        """Sets up test methods."""
        pass

    def tearDown(self):
        """Tears down test methods."""
        self.resetStorage()
        pass

    def reset_Storage(self):
        """Resets FileStorage data"""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_instant(self):
        """Tests instantiation of Amenity class."""

        b = Amenity()
        self.assertEqual(str(type(b)), "<class 'models.amenity.Amenity'>")
        self.assertIsInstance(b, Amenity)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_two_amenities_unique_ids(self):
        amenity1 = Amenity()
        amenity2 = Amenity()
        self.assertNotEqual(amenity1.id, amenity2.id)

    def test_str_representation(self):
        my_date = datetime.today()
        my_date_repr = repr(my_date)
        amenity1 = Amenity()
        amenity1.id = "1963778"
        amenity1.created_at = amenity1.updated_at = my_date
        amenity_str = amenity1.__str__()
        self.assertIn("[Amenity] (1963778)", amenity_str)
        self.assertIn("'id': '1963778'", amenity_str)
        self.assertIn("'created_at': " + my_date_repr, amenity_str)
        self.assertIn("'updated_at': " + my_date_repr, amenity_str)

    def test_attributes(self):
        """Tests the attributes of Amenity class"""
        attributes = storage.attributes()["Amenity"]
        X = Amenity()
        for i, j in attributes.items():
            self.assertTrue(hasattr(X, i))
            self.assertEqual(type(getattr(X, i, None)), j)


if __name__ == "__main__":
    unittest.main()
