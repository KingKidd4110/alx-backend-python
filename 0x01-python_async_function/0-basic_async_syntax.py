#!/usr/bin/env python3
""" Asyncronous co-routine for random delay"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    use random module
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
