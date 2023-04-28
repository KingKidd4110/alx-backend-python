#!/usr/bin/env python3
""" takes a float multiplier as argument """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], [float]]:
    """ Returns a function that multiplies a float by multiplier """
    def make_func(number: float) -> float:
        return multiplier * number
    return make_func
