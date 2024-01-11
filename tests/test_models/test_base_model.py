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
        date_repr = repr(datetime.today())
        BM = BaseModel()
        BM.id = "0123456"
        BM.created_at = BM.updated_at = datetime.today()
        bm_str = BM.__str__()
        self.assertIn("[BaseModel] (0123456)", bm_str) 
        self.assertIn("'id': '0123456'", bm_str)
        self.assertIn("'created_at': " + date_repr, bm_str)
        self.assertIn("'updated_at': " + date_repr, bm_str)


if __name__ == "__main__":
    unittest.main()
