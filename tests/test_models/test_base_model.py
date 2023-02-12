#!/usr/bin/python3
"""test module for BaseModel"""
import unittest
from models.base_model import BaseModel
import uuid
import datetime


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
        """test updated_at"""
        model = BaseModel()
        updated_at = model.updated_at
        model.save()
        self.assertNotEqual(updated_at, model.updated_at)

    def test_add_attribute(self):
        """test add attribute"""
        model = BaseModel()
        model.first_name = 'Musa'
        model.last_name = 'Ibrahim'
        self.assertTrue(hasattr(model, 'first_name'))
        self.assertTrue(hasattr(model, 'last_name'))

    def test_create_from_dict(self):
        model1 = BaseModel()
        model1.spent = 3000
        model1.first_name = 'Musa'
        model1.last_name = 'Ibrahim'
        model1_dict = model1.to_dict()
        model2 = BaseModel(**model1_dict)
        self.assertAlmostEqual(model1_dict, model2.to_dict())
        self.assertEqual(model1.created_at, model2.created_at)
        self.assertEqual(model1.updated_at, model2.updated_at)
        self.assertEqual(model1.first_name, model2.first_name)
        self.assertEqual(model1.spent, model2.spent)
        self.assertEqual(model1.id, model2.id)
