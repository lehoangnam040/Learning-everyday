import aiofiles
import aiofiles.os
import asyncio


async def main():
    try:
        _f = await aiofiles.open("./ab/asd.txt", "wb")
    except Exception as err:
        print("exception", err, type(err))
    else:
        await _f.write(b"asfasdsa")
        await _f.close()

    print("finish")


asyncio.run(main())