import asyncio
import threading
import time

def sync_f(a=None):
    # time.sleep is bugged, this is an ugly-but-working way of getting an actual sleep.
    lock = threading.Lock()
    lock.acquire(blocking=False)
    # 
    for _ in range(5):
        # time.sleep
        print("call f")
        lock.acquire(timeout=1)

    return 4

async def async_g(a=None):
    for _ in range(5):
        print("call g")
        await asyncio.sleep(1)
    return 1

async def main():
    # loop = asyncio.get_running_loop()
    results = await asyncio.gather(
        async_g(),
        # loop.run_in_executor(None, sync_f),
        asyncio.to_thread(sync_f),
    )
    print(max(results))

if __name__ == '__main__':
    asyncio.run(main())