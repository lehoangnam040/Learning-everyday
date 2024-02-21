import asyncio
import uvloop   # 0.14.0
import threading
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
        self.task = asyncio.Task(coroutine, loop=loop)
        self.notifier = threading.Condition()

class Handler:

    def __init__(self, loop: asyncio.AbstractEventLoop) -> None:
        self.loop = loop
        self.fetchers: Dict[int, DownloaderMetadata] = dict()

    async def download_logic(self, url: str, key: int) -> int:
        async with ClientSession() as session:
            async with session.get(url) as response:
                with open(f"{key}.json", "wb") as _f:
                    async for chunk in response.content.iter_chunked(512):
                        self.fetchers[key].progress += len(chunk)
                        _f.write(chunk)
                        with handler.fetchers[key].notifier:
                            self.fetchers[key].notifier.notify_all()
        with handler.fetchers[key].notifier:
            self.fetchers[key].notifier.notify_all()

    def start_download_model(self, key: int):
        self.fetchers[key] = DownloaderMetadata(loop, self.download_logic('https://raw.githubusercontent.com/json-iterator/test-data/master/large-file.json', key))

    def read_progress(self, key: int) -> int:
        return self.fetchers[key].progress

    async def cancel_download_model(self, key: int):
        task = self.fetchers[key].task
        print("is done before cancel", task.done())
        if task.done():
            return
        task.cancel()
        try:
            await task
        except asyncio.CancelledError:
            print("cancelled now")

def grpc_subscribe_func(thread_identify: str, handler: Handler, key: int):
    while True:
        if handler.fetchers[key].task.done():
            print("finished", thread_identify, handler.fetchers[key].task.done())
            break
        with handler.fetchers[key].notifier:
            handler.fetchers[key].notifier.wait()
        progress = handler.read_progress(key)
        print("read_progress", thread_identify, progress, handler.fetchers[key].task.done())

def grpc_cancel_func(handler: Handler, key: int):
    asyncio.run_coroutine_threadsafe(handler.cancel_download_model(key), handler.loop)

if __name__ == "__main__":
    # PYTHON 3.6
    uvloop.install()
    loop = asyncio.new_event_loop()

    asyncio_thread = AsyncioThread(loop)
    asyncio_thread.start()

    handler = Handler(loop)

    key = 30
    handler.start_download_model(key)

    t1 = threading.Thread(target=grpc_subscribe_func, args=("t1", handler, key))
    t2 = threading.Thread(target=grpc_subscribe_func, args=("t2", handler, key))
    t1.start()
    t2.start()
    t2.join()
    t1.join()
