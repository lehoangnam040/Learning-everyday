import asyncio
from concurrent.futures import ProcessPoolExecutor
import functools

def cpu_intensive_task(count_to: int):
    counter = 0
    while counter < count_to:
        counter += 1
    return counter

async def main():
    with ProcessPoolExecutor() as executor:
        loop = asyncio.get_running_loop()
        nums = [1, 3, 5, 22, 10000000]

        call_coros = []
        for num in nums:
            call_coros.append(loop.run_in_executor(executor, functools.partial(cpu_intensive_task, num)))
        
        results = await asyncio.gather(*call_coros)
        for res in results:
            print(res)

if __name__ == "__main__":
    asyncio.run(main())