#!/usr/bin/python3
"""test state module"""
from unittest import TestCase
from models.state import State
import os

class TestState(TestCase):
    """test State module"""

    @classmethod
    def setUp(cls):
        """setupp method"""
        cls.state = State()
        cls.state.name = 'Kogi'

    @classmethod
    def tearDown(cls):
        try:
            os.remove('file.json')
        except FileNotFoundError:
            raise FileNotFoundError('File no found')

    
    def test_object_created(self):
        """test object is created and """
        self.assertTrue(hasattr(self.state, 'name'))
        self.assertTrue(hasattr(self.state, 'to_dict'))
        self.assertTrue(hasattr(self.state, 'save'))

    def test_to_dict(self):
        """test to_dict method"""
        self.state.save()
        state_json = self.state.to_dict()
        new_state = State(**state_json)
        self.assertAlmostEqual(state_json, new_state.to_dict())
        self.assertTrue(os.path.isfile('file.json'))

