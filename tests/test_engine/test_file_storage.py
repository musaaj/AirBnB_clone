#!/usr/bin/python3
"""Test File Storage"""
import unittest
import models
from models.user import User
from models.engine.file_storage import FileStorage
from datetime import datetime
import os


class TestFileStorage(unittest.TestCase):
    """unit test"""
    def test_doc1(self):
        """test docstring for module"""
        res = "Module has no documentation"
        self.assertIsNotNone(models.engine.file_storage.__doc__, res)

    def test_doc2(self):
        """test docstring for class"""
        res = "Class has no documentation"
        doc = FileStorage.__doc__
        self.assertIsNotNone(doc, res)

    def test_doc3(self):
        """test documentation for methods"""
        res = "all method has no documentation"
        func = FileStorage.all.__doc__
        self.assertIsNotNone(func, res)

        res = "new method has no documentation"
        function = FileStorage.new.__doc__
        self.assertIsNotNone(function, res)

        res = "save method has no documentation"
        function = FileStorage.save.__doc__
        self.assertIsNotNone(function, res)

        res = "reload method has no documentation"
        function = FileStorage.reload.__doc__
        self.assertIsNotNone(function, res)
 
    def test_instance1(self):
        """test instance"""
        storage = FileStorage()
        self.assertIsInstance(storage, FileStorage)

    @classmethod
    def setUps(cls):
        """set up for test"""
        cls.user = User()
        cls.user.first_name = "Musa"
        cls.user.last_name = "Ibrahim"
        cls.user.email = "musaaj@gmail.com"
        cls.storage = FileStorage()
        cls.path = "file.json"


if __name__ == "__main__":
    unittest.main()
