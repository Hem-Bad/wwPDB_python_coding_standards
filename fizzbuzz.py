#!/usr/bin/env python3

from typing import Union


def fizzbuzz(number):
    """ The classic FizzBuzz method.

    Returns FizzBuzz, Fizz, Buzz, or the input number for numbers greater than zero.
    Raises ValueError for numbers less than 10."""
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    elif number < 0:
        raise ValueError("Cannot FizzBuzz numbers less than 0.")


fizzbuzz.__annotations__ = {'number': int, 'return': Union[str, int]}

