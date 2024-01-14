#!/usr/bin/python3
"""Unittest module for the User Class."""

from datetime import datetime
from time import sleep
import os
import unittest
from models.user import User


class Test_User(unittest.TestCase):

    def setUp_User(self):
        """Sets up test methods."""
        pass

    def reset_User(self):
        """reset user test methods."""
        self.resetStorage()
        pass

    def reset_Storage(self):
        """Resets storage data"""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_for_instantiation(self):
        """Tests instantiation of User class."""
        user = User()
        self.assertEqual(str(type(user)), "<class 'models.user.User'>")
        self.assertIsInstance(user, User)
        self.assertTrue(issubclass(type(user), BaseModel))

    def test_save(self):
        self.user.save()
        self.assertNotEqual(self.user.created_at, self.user.updated_at)

    def test_two_users_created(self):
        user1 = User()
        sleep(0.05)
        user2 = User()
        self.assertLess(user1.created_at, user2.created_at)


if __name__ == "__main__":
    unittest.main()
