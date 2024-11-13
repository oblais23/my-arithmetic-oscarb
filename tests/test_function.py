"""
Test module for function
"""

from src.my_arithmetic_oscarb.function import (pgcd)
from unittest import TestCase


class TestFunctions(TestCase):
    def test_valid_pgcd(self):
        self.assertEqual(34, pgcd(40902, 24140))

    def test_invalid_pgcd(self):
        self.assertNotEqual(0, pgcd(40902, 24140))

    def test_valid_pgcd2(self):
        self.assertEqual(34, pgcd(40902, 24140))

    def test_invalid_pgcd2(self):
        self.assertNotEqual(0, pgcd(40902, 24140))

    def test_valid_pgcd3(self):
        self.assertEqual(34, pgcd(40902, 24140))

    def test_invalid_pgcd3(self):
        self.assertNotEqual(0, pgcd(40902, 24140))

    def test_valid_pgcd4(self):
        self.assertEqual(34, pgcd(40902, 24140))

    def test_invalid_pgcd4(self):
        self.assertNotEqual(0, pgcd(40902, 24140))

    def test_valid_pgcd5(self):
        self.assertEqual(34, pgcd(40902, 24140))

    def test_invalid_pgcd5(self):
        self.assertNotEqual(0, pgcd(40902, 24140))

    def test_valid_pgcd6(self):
        self.assertEqual(34, pgcd(40902, 24140))

    def test_invalid_pgcd6(self):
        self.assertNotEqual(0, pgcd(40902, 24140))

    def test_valid_pgcd7(self):
        self.assertEqual(34, pgcd(40902, 24140))

    def test_error(self):
        self.assertEqual(1, 2)