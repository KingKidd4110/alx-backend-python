#!/usr/bin/env python3
"""  execute async_comprehension four times in parallel """
import asyncio
import random
async_comprehension = __import__('1-async_comprehension').async_comprehension
async_generator = __import__('0-async_generator').async_generator


async def measure_runtime() -> float:
    """
    execute async_comprehension four times in parallel using asyncio.gather
    """
    start_time = asyncio.get_running_loop().time()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    end_time = asyncio.get_running_loop().time()
    return end_time - start_time
