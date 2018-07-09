#!/usr/bin/env python3

import sys
import unittest
from os import path

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
import fizzbuzz


class FizzBuzzTest(unittest.TestCase):

    def test_fizz(self):
        self.assertEqual("Fizz", fizzbuzz.fizzbuzz(3))

    def test_buzz(self):
        self.assertEqual("Buzz", fizzbuzz.fizzbuzz(5))

    def test_fizzbuzz(self):
        self.assertEqual("FizzBuzz", fizzbuzz.fizzbuzz(15))

    def test_other(self):
        self.assertEqual(2, fizzbuzz.fizzbuzz(2))

    def test_negative(self):
        with self.assertRaises(ValueError):
            fizzbuzz.fizzbuzz(-1)
