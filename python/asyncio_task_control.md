# First things first: Theory

- awaitable `asyncio.gather`:
  - run awaitable objects in the sequence concurrently
  - return list of return values, with corresponds to the order of awaitable objects
  - different with `TaskGroup`: in `TaskGroup`, if a task raises Exception, `TaskGroup` will cancel remaining scheduled tasks, while `gather` will NOT

- coroutine `asyncio.wait`:
  - run `Future` / `Task` concurrently and block until condition of `return_when`
  - return (`done`, `pending`)

- `asyncio.as_completed`:
  - return iterator of `coroutines`, each coroutine can be `await` to get earliest result

- coroutine `asyncio.to_thread`:
  - run a function in a separate thread, make it as coroutine
  - to avoid block event loop
  - due to GIL, it should be used to make IO-bound non-blocking / call C++/Rust modules

- `asyncio.run_coroutine_threadsafe`:
  - submit a coroutine to the given event loop. thread-safe
  - return `Future` to wait for the result
  - this function will be called from different OS thread where event loop is running

# References:

- https://docs.python.org/3/library/asyncio-task.html