#!/usr/bin/python3
"""
Unittest module for the BaseModel Class and its methods
"""
from models.base_model import BaseModel
from datetime import datetime
import unittest


class TestBasemodel(unittest.TestCase):
    """
    Unittest cases for BaseModel
    """

    def test_init(self):
        """
        unittest for init
        """
        BM = BaseModel()
        self.assertIsNotNone(BM.id)
        self.assertIsNotNone(BM.created_at)
        self.assertIsNotNone(BM.updated_at)

    def test_str_repr(self):
        """
        str repersentation test
        """
        date_time = datetime.today()
        dt_repr = repr(date_time)
        BM = BaseModel()
        BM.id = "123456"
        BM.created_at = BM.updated_at = date_time
        BM_str = BM.__str__()
        self.assertIn("[BaseModel] (123456)", BM_str)
        self.assertIn("'id': '123456'", BM_str)
        self.assertIn("'created_at': " + dt_repr, BM_str)
        self.assertIn("'updated_at': " + dt_repr, BM_str)

    def test_save(self):
        """
        save method test
        """
        BM = BaseModel()
        initial_updated_at = BM.updated_at
        current_updated_at = BM.save()
        self.assertNotEqual(initial_updated_at, current_updated_at)

    def test_3_to_dict(self):
        """Tests the public method to_dict()"""
        BM = BaseModel()
        BM.name = "hadeer"
        BM.age = 30
        X = BM.to_dict()
        self.assertEqual(X["id"], BM.id)
        self.assertEqual(X["__class__"], type(BM).__name__)
        self.assertEqual(X["created_at"], BM.created_at.isoformat())
        self.assertEqual(X["updated_at"], BM.updated_at.isoformat())
        self.assertEqual(X["name"], BM.name)
        self.assertEqual(X["age"], BM.age)


if __name__ == "__main__":
    unittest.main()
