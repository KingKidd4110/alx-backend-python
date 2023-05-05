#!/usr/bin/env python3
""" takes in an integer and returns asyncio.task """
import asyncio
from random import randint
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    """
    function
    """
    return asyncio.ensure_future(wait_random(max_delay))
