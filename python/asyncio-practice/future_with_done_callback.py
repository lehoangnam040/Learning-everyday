import asyncio
import aiofiles
import aiofiles.os
import pathlib
import threading
import logging
import signal

logger = logging.getLogger(__name__)

async def _coro(_loop):
    print("start _coro")
    _tmp = pathlib.Path() / "_tmp_abc"
    _save = pathlib.Path() / "abc"
    async with aiofiles.open(_tmp, "wb", loop=_loop) as _f:
        for _ in range(20):
            await _f.write(b"-")
            print("-------")
            await asyncio.sleep(1)
    await aiofiles.os.replace(_tmp, _save, loop=_loop)
    

async def _coro_done(asyncio_futu, _loop):
    _tmp = pathlib.Path() / "_tmp_abc"
    if _tmp.exists():
        print("need delete")
        await aiofiles.os.remove(_tmp, loop=_loop)
    else:
        print("deleted, not exists")
    asyncio_futu.set_result("finished")


class X(threading.Thread):

    def __init__(self, asyncio_futu, _loop) -> None:
        super().__init__(target=self.another_thread, args=(asyncio_futu, _loop, ), name="Some_Thread")

    def another_thread(self, asyncio_futu, _loop):
        self._futu = asyncio.run_coroutine_threadsafe(_coro(_loop), _loop)
        self._futu.add_done_callback(lambda _: asyncio.run_coroutine_threadsafe(_coro_done(asyncio_futu, _loop), _loop))
        print("finish another thread")

    def cancel(self):
        print("go to cancel")
        self._futu.cancel()

async def main():
    asyncio_futu = asyncio.Future()

    logger.setLevel(logging.DEBUG)
    _loop = asyncio.get_running_loop()
    print(_loop, _loop.is_running())

    x = X(asyncio_futu, _loop)
    def graceful_shutdown(*args, **kwargs):
        print("graceful_shutdown")
        x.cancel()
        asyncio_futu.set_result("ended by cancel")
    for _sig in [signal.SIGINT, signal.SIGTERM]:
        signal.signal(_sig, graceful_shutdown)

    x.start()

    await asyncio_futu
    print("finished", asyncio_futu.result())
    

if __name__ == "__main__":
    asyncio.run(main())