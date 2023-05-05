#!/usr/bin/env python3
""" imports wait_n """
import asyncio
import time
from typing import List
from random import randint
from itertools import repeat
wait_n = __import__('1-concurrent_coroutines').wait_n
wait_random = __import__('0-basic_async_syntax').wait_random


async def measure_time(n: int, max_delay: int) -> float:
    """ Measure_time function returns approx time"""
    start_time = time.time()

    delays = await wait_n(n, max_delay=max_delay)
    total_time = end_time - start_time

    return total_time / n
