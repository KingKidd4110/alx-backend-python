#!/usr/bin/env python3
""" async_generator co-routine """
import asyncio
import random


async def async_generator() -> None:
    """
    The coroutine takes no arguments
    loops = 10 asyncronously
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
