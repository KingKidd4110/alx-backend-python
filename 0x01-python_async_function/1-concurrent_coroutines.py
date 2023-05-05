#!/usr/bin/env python3
""" Async taking two arguments """
import asyncio
from typing import List
from random import randint
from itertools import repeat
from datetime import datetime
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    wait_n uses wait_random function
    """
    delays = await asyncio.gather(*repeat(wait_random(max_delay), n))
    return sorted(delays)
