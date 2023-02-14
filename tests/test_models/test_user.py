#!/usr/bin/python3
"""unit test for user module"""
from models.user import User
from unittest import TestCase
import os
from datetime import datetime


class TestUser(TestCase):
    """unit test for User model"""

    @classmethod
    def setUp(cls):
        cls.user = User()
        cls.user.first_name = 'Musa'
        cls.user.last_name = 'Ibrahim'
        cls.user.save()

    @classmethod
    def tearDown(cls):
        try:
            os.remove('file.json')
        except FileNotFoundError:
            raise AssertionError('File not found')

    def test_object_created(self):
        """test self.user is created"""
        self.assertTrue(self.user)
        self.assertTrue(hasattr(self.user, 'updated_at'))
        self.assertTrue(type(self.user.to_dict()) is dict)

    def test_save(self):
        """test User save method"""
        self.user.save()
        self.assertTrue(os.path.isfile('file.json'))

    def test_to_dict(self):
        """test to_dict method"""
        user_json = self.user.to_dict()
        self.assertIsInstance(user_json['updated_at'], str)
        self.assertFalse(user_json.get('email'))
        user = User(**user_json)
        self.assertTrue(self.user.id == user.id)
        self.assertTrue(user.first_name == self.user.first_name)
        self.assertTrue(user.created_at == self.user.created_at)
        self.assertTrue(str(user) == str(self.user))
