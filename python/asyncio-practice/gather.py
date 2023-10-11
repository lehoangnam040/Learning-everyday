import asyncio


async def call_api(i: int) -> int:
    await asyncio.sleep(i)

    if i == 7:
        raise Exception("mock exception")
    return i * 2


async def main():
    tasks = [call_api(i) for i in range(10)]

    results = await asyncio.gather(*tasks, return_exceptions=True)
    exceptions = [res for res in results if isinstance(res, Exception)]
    success_results = [res for res in results if not isinstance(res, Exception)]

    print(results)
    print(exceptions)
    print(success_results)

if __name__ == '__main__':
    asyncio.run(main())