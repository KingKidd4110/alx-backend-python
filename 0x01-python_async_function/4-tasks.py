#!/usr/bin/env python3
""" Altering wait_n """
import asyncio
from typing import List
from intertools import repeat
task_wait_random = __import__('3-tasks.py').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    Alters wait_n to call task wait_n
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
