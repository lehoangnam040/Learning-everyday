import asyncio


async def _task(future):

    await asyncio.sleep(2)
    future.set_result(123)

def create_future():
    future = asyncio.Future()
    asyncio.create_task(_task(future))
    return future

async def main():
    future = create_future()
    print(future.done())

    value = await future
    print(future.done())
    print(value)


if __name__ == '__main__':
    asyncio.run(main())