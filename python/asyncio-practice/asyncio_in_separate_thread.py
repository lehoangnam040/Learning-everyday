import asyncio
import uvloop   # 0.14.0
import threading
import signal
from aiohttp import ClientSession

from typing import Dict

class AsyncioThread(threading.Thread):

    def __init__(self, loop: asyncio.AbstractEventLoop) -> None:
        super().__init__(daemon=True)
        self.loop = loop

    def run(self) -> None:
        self.loop.run_forever()


class DownloaderMetadata:

    def __init__(self, loop: asyncio.AbstractEventLoop, coroutine, *args, **kwargs) -> None:
        self.progress = 0
        # need to ensure future after create condition
        self.notifier = threading.Condition()
        # self.task: "asyncio.Task" = asyncio.ensure_future(coro_or_future=coroutine, loop=loop)
        self.task = asyncio.run_coroutine_threadsafe(coro=coroutine, loop=loop)

class Handler:

    def __init__(self, loop: asyncio.AbstractEventLoop) -> None:
        self.loop = loop
        self.fetchers: Dict[int, DownloaderMetadata] = dict()

    def notify_all(self, key: int):
        with self.fetchers[key].notifier:
            self.fetchers[key].notifier.notify_all()

    async def download_logic(self, url: str, key: int) -> None:
        async with ClientSession() as session:
            async with session.get(url) as response:
                with open(f"{key}.json", "wb") as _f:
                    async for chunk in response.content.iter_chunked(512):
                        self.fetchers[key].progress += len(chunk)
                        _f.write(chunk)
                        await self.loop.run_in_executor(None, self.notify_all, key)
        self.loop.run_in_executor(None, self.notify_all, key)

    def start_download_model(self, key: int):
        self.fetchers[key] = DownloaderMetadata(self.loop, self.download_logic('https://raw.githubusercontent.com/json-iterator/test-data/master/large-file.json', key))

    def read_progress(self, key: int) -> int:
        return self.fetchers[key].progress

    def cancel_download_model(self, key: int):
        print(self.fetchers[key].task.running())
        print(self.fetchers[key].task.cancel())
        self.notify_all(key)
        print(self.fetchers[key].task.running())

def grpc_subscribe_func(thread_identify: str, handler: Handler, key: int):
    while True:
        if handler.fetchers[key].task.done():
            print("finished", thread_identify, handler.fetchers[key].task.done())
            break
        with handler.fetchers[key].notifier:
            handler.fetchers[key].notifier.wait()
        progress = handler.read_progress(key)
        print("read_progress", thread_identify, progress, handler.fetchers[key].task.done())

if __name__ == "__main__":
    # PYTHON 3.6
    uvloop.install()
    loop = asyncio.new_event_loop()

    asyncio_thread = AsyncioThread(loop)
    asyncio_thread.start()

    handler = Handler(loop)
    key = 31

    def graceful_shutdown(*args, **kwargs):
        print("graceful_shutdown")
        handler.cancel_download_model(key)
        # loop.stop()   # comment this to test
    for _sig in [signal.SIGINT, signal.SIGTERM]:
        signal.signal(_sig, graceful_shutdown)

    handler.start_download_model(key)

    t1 = threading.Thread(target=grpc_subscribe_func, args=("t1", handler, key))
    t2 = threading.Thread(target=grpc_subscribe_func, args=("t2", handler, key))
    t1.start()
    t2.start()
    t2.join()
    t1.join()
