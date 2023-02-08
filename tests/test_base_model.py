#!/usr/bin/python3
"""test module for BaseModel"""
import unittest
from models.base_model import BaseModel
import uuid
import datetime


class TestBaseModel(unittest.TestCase):
    """test class for BaseModel"""

    def test_class_created(self):
        model = BaseModel()
        self.assertEqual(model.__class__.__name__, 'BaseModel')
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime.datetime)
