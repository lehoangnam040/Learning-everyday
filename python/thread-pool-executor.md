
# First things first: Theory

- `ThreadPoolExecutor` is an `Executor` subclass, use pool of threads to execute call async
- deadlocks can occur if bugs in code
- exceptions in main thread must be caught and handled in order to signal threads to exit gracefully -> recommend this class should NOT be used for long-running tasks

## How it works

- tasks are sent into the pool by adding them to an internal queue
- worker threads are created on-demand and reuse when a task is completed and another task coming

## Usage Pattern

- Map and wait
  - most common pattern
  - Code: `for result in executor.map(task, list_of_args):`
  - issue all tasks to the threadpool immediately, 
- Submit and use as completed
  - `submit()` to push tasks into the pool, return `Future` objects
  - call `as_completed(futures)` return as its task is completed
- Submit and use sequentially
  - `submit()` to push tasks into the pool, return `Future` objects
  - using iterator like `for future in futures` instead of `as_completed` to return results in order
- Submit and use callback
  - `submit()` and call `future.add_done_callback`
- Submit and wait for all
  - `submit()` and call `wait(futures)` to block until some conditions are meet
- Submit and wait for first
  - `submit()` and call `wait(futures, return_when=FIRST_COMPLETED)` 

# References

- https://superfastpython.com/threadpoolexecutor-in-python/