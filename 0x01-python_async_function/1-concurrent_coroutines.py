#!/usr/bin/env python3
"""An example of waiting for multiple tasks in parallel"""

import asyncio
import random
from typing import List

# Import the wait_random coroutine from the previous example
wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    Waits for a random delay between 0 and max_delay (float value) seconds
    n times, and returns a list of the actual delays that were waited.
    """
    # Create an empty list to hold the delayed tasks and the actual delays
    spawn_list = []
    delay_list = []

    # Create n delayed tasks, and add a callback to record the actual delay
    for i in range(n):
        delayed_task = asyncio.create_task(wait_random(max_delay))
        delayed_task.add_done_callback(lambda x: delay_list.append(x.result()))
        spawn_list.append(delayed_task)

    # Wait for all of the delayed tasks to complete
    for spawn in spawn_list:
        await spawn

    # Return the list of actual delays
    return delay_list
