# First things first: Theory

- it's the core of every asyncio application
- default with 2 different loop implementations: `SelectorEventLoop` (Unix) & `ProactorEventLoop` (Windows)

# Code

- `loop.run_until_complete`
  - run until the future argument has completed
- `loop.run_forever`
  - run the event loop until `stop()` is called
- Scheduling callbacks
  - `loop.call_soon`
  - `loop.call_soon_threadsafe`
- Scheduling delayed callbacks
  - `loop.call_later`
  - `loop.call_at`
- Create futures and tasks
  - `loop.create_future`
  - `loop.create_task`
- Unix signals
  - `loop.add_signal_handler`
- Execute code in thread or process pools
  - awaitable `loop.run_in_executor`
  - 

# References:
- https://docs.python.org/3/library/asyncio-eventloop.html