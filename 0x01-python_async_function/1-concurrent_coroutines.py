#!/usr/bin/env python3
""" Async taking two arguments """
import asyncio
from typing import List
from random import randint
from itertools import repeat
from datetime import datetime


async def wait_random(max_delay: int = 10) -> float:
    delay = randint(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    delays = await asyncio.gather(*repeat(wait_random(max_delay), n))
    return sorted(delays)
