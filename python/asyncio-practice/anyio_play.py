import asyncio
import anyio
from anyio import open_file
from anyio import from_thread, to_thread
import uvloop

async def play_file():
    try:
        _f = await open_file("./ab/cdec.txt", "w")
    except Exception as err:
        print("except open_file", err)
    else:
        async with _f:
            await _f.write("bcadssad")

    print("finish")

async def async_gen_foo():

    for i in range(3):
        await asyncio.sleep(1)
        yield i+1
    yield

def main_blocking():
    uvloop.install()
    foo = async_gen_foo()
    with from_thread.start_blocking_portal() as portal:
        while True:
            x = portal.call(foo.__anext__)
            print(x)
            if x is None:
                print("****")
                break
            print("----")
    print("goodbye")


main_blocking()
# asyncio.run(play_file())
