#!/usr/bin/python3
"""test module for BaseModel"""
import unittest
from models.base_model import BaseModel
import uuid
import datetime
"Authors henok934 & musaaj"""



class TestBaseModel(unittest.TestCase):
    """test class for BaseModel"""

    def test_instance_created(self):
        """test if object is created"""
        model = BaseModel()
        self.assertEqual(model.__class__.__name__, 'BaseModel')
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime.datetime)
        self.assertIsInstance(model.updated_at, datetime.datetime)

    def test_to_dict(self):
        """test BaseModel to_dict method"""
        model = BaseModel()
        self.assertIsInstance(model.to_dict(), dict)

    def test_updated_at(self):
        model = BaseModel()
        updated_at = model.updated_at
        model.save()
        self.assertNotEqual(updated_at, model.updated_at)
