import asyncio


async def call_api(i: int) -> int:

    for _ in range(10 - i):
        await asyncio.sleep(1)
        print("-----", i)

    if i == 7:
        raise Exception("mock exception")
    return i * 2


async def main():
    tasks = [call_api(i) for i in range(10)]

    for done_task in asyncio.as_completed(tasks):
        try:
            res = await done_task
            print(res)
        except Exception as err:
            print("catch ex: ", err)

if __name__ == '__main__':
    asyncio.run(main())