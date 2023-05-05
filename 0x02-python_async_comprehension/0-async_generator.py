#!/usr/bin/env python3
""" async_generator co-routine """
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    The coroutine takes no arguments
    Generator loop 10 times asyncronously
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
