#!/usr/bin/env python3
"""An example of combining an asynchronous coroutine with a synchronous function"""

import asyncio
import random
from typing import List


# Import the wait_random coroutine from the previous example
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int = 0, max_delay: int = 10) -> List[float]:
    """
    Waits for a random delay between 0 and max_delay (float value) seconds
    n times, and returns a list of the actual delays that were waited.
    """
    # Create an empty list to hold the delays
    delays: List[float] = []

    # Create a list of tasks that will each wait for a random delay
    tasks: List = []
    for _ in range(n):
        tasks.append(wait_random(max_delay))

    # Wait for all of the tasks to complete, and record the actual delays
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    # Return the list of actual delays
    return delays
