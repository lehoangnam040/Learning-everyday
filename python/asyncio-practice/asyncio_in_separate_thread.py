import asyncio
import uvloop   # 0.14.0
import threading
from aiohttp import ClientSession

class AsyncioThread(threading.Thread):

    def __init__(self, loop: asyncio.AbstractEventLoop) -> None:
        super().__init__(daemon=True)
        self.loop = loop

    def run(self) -> None:
        self.loop.run_forever()

class Handler:

    def __init__(self, loop: asyncio.AbstractEventLoop) -> None:
        self.loop = loop
        self.fetchers = dict()

    async def download_logic(self, url: str, key: int) -> int:
        print("start logic")
        for _ in range(key):
            self.fetchers[key]["progress"] += 1
            with handler.fetchers[limit]["notifier"]:
                self.fetchers[key]["notifier"].notify_all()
            await asyncio.sleep(1)
            print("progress inc")
        async with ClientSession() as session:
            async with session.get(url) as response:
                print("done logic", response.status)
        with handler.fetchers[limit]["notifier"]:
            self.fetchers[key]["notifier"].notify_all()

    def start_download_model(self, key: int):
        self.fetchers[key] = {
            "progress": 0,
            "notifier": threading.Condition(),
        }
        self.fetchers[key]["asyncio_task"] = asyncio.Task(self.download_logic(f'http://httpbin.org/delay/2', key), loop=self.loop)      # python 3.6 

    def read_progress(self, key: int) -> int:
        return self.fetchers[key]["progress"]

    async def cancel_download_model(self, key: int):
        task = self.fetchers[key]["asyncio_task"]
        print("is done before cancel", task.done())
        if task.done():
            return
        task.cancel()
        try:
            for _ in range(2):
                print("-----", task.done())
                await asyncio.sleep(1)
            await task
        except asyncio.CancelledError:
            print("cancelled now")

def grpc_subscribe_func(thread_identify: str, handler: Handler, key: int):
    while True:
        if handler.fetchers[key]["asyncio_task"].done():
            print("finished", thread_identify, handler.fetchers[key]["asyncio_task"].done())
            break
        with handler.fetchers[key]["notifier"]:
            handler.fetchers[key]["notifier"].wait()
        progress = handler.read_progress(key)
        print("read_progress", thread_identify, progress, handler.fetchers[key]["asyncio_task"].done())

def grpc_cancel_func(handler: Handler, key: int):
    asyncio.run_coroutine_threadsafe(handler.cancel_download_model(key), handler.loop)

if __name__ == "__main__":
    # PYTHON 3.6
    uvloop.install()
    loop = asyncio.new_event_loop()

    asyncio_thread = AsyncioThread(loop)
    asyncio_thread.start()

    handler = Handler(loop)

    limit = 30
    handler.start_download_model(limit)

    t1 = threading.Thread(target=grpc_subscribe_func, args=("t1", handler, limit))
    t2 = threading.Thread(target=grpc_subscribe_func, args=("t2", handler, limit))
    t1.start()
    t2.start()
    t2.join()
    t1.join()
