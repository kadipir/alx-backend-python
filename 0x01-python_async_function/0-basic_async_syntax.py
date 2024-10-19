#/usr/bin/env python3

import asyncio
import random

async def wait_random(max_delay : int = 10) -> float:
    wait = random.random() * max_delay
    asyncio.sleep(wait)
    return (wait)
