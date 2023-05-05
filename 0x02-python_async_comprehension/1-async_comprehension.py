#!/usr/bin/env python3
""" modification of previous async """
import asyncio
import random
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    collect 10 random numbers using an async
    comprehensing over async_generator  returns the 10 random numbers
    """
    result = [number async for number in async_generator()]
    return result
