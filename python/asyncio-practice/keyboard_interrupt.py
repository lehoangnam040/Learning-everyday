import asyncio

async def main():

    print("hello")
    for _ in range(10):
        print("---")
        await asyncio.sleep(1)
    print("world")

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt as err:
        print("catch err", err)
