#!/usr/bin/python3
"""Unit tests for helper.parseline module"""
from helper.line_parser import parse_line
from unittest import TestCase


class TestParser(TestCase):
    """test parse_line function"""

    def test_return_type(self):
        """test list is returned"""
        result = parse_line('Hello "my word" by')
        self.assertIsInstance(result, list)
        length = len(result)
        self.assertEqual(length, 3)

    def test_pass_int(self):
        """test integer passed"""
        result = parse_line(120)
        self.assertIsInstance(result, list)
        length = len(result)
        self.assertEqual(length, 0)

    def test_none_passed(self):
        """test none passed"""
        result = parse_line(None)
        self.assertFalse(result)
        self.assertFalse(len(result))

    def test_invalid_str(self):
        """test invalid string passed"""
        result = parse_line('Hi "Not closed')
        self.assertEqual(result, ['Hi', 'Not closed'])
        result = parse_line('Hello w"orld"!')
        self.assertEqual(result, ['Hello', 'w"orld"!'])

