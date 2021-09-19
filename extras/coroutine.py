
import asyncio
from time import time
async def sleeper_coroutine():
    """ Jsut a simple coroutine to explore asyncio"""
    print("enter sleeper coroutine")
    await asyncio.sleep(5)
    print("finish coroutine")


if __name__ == '__main__':
    start_t = time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(sleeper_coroutine())
    print("ends in {}".format(time()-start_t))

