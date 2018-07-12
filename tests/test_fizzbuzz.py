#!/usr/bin/env python3

import sys
import unittest
from os import path

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
import fizzbuzz


class FizzBuzzTest(unittest.TestCase):

    def test_fizzbuzz_function(self):
        self.assertEqual("Fizz", fizzbuzz.fizzbuzz(3))
        self.assertEqual("Buzz", fizzbuzz.fizzbuzz(5))
        self.assertEqual("FizzBuzz", fizzbuzz.fizzbuzz(15))
        self.assertEqual(2, fizzbuzz.fizzbuzz(2))
        with self.assertRaises(ValueError):
            fizzbuzz.fizzbuzz(-1)

