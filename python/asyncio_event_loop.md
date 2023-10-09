# First things first: Theory

- it's the core of every asyncio application
- when create an event loop, we creates empty queue of tasks
- each iteration of loop checks for tasks that need to be run and will run them until a task hits an I/O operation
- this task will be paused, instruct OS to wait socket of it to complete
- then execute another task on queue
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