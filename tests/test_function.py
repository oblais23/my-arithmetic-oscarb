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