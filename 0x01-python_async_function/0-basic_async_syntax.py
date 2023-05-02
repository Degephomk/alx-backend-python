#!/usr/bin/env python3
"""An example of an asynchronous coroutine in Python"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and max_delay (float value) seconds
    and eventually returns the delay.
    """
    # Generate a random delay between 0 and max_delay
    actual_delay: float = random.uniform(0, max_delay)

    # Suspend the execution of this coroutine for the given delay
    await asyncio.sleep(actual_delay)

    # Return the actual delay that was waited
    return actual_delay
