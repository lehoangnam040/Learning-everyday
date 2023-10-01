
# First things first: Theory

- `ProcessPoolExecutor` is an `Executor` subclass, use pool of processes to execute call async
- using `multiprocessing` module inside

## How it works

- when submit task, pool will add task to an internal dictionary with unique identifier
- pool has an internal worker thread that will retrieve new task and submit to a queue
- queue contains the task to be executed by worker processes
- worker processes are created on-demand and reuse when a task is completed and another task coming

## Usage Pattern

- Map and wait
  - most common pattern
  - Code: `for result in executor.map(task, list_of_args):`
  - issue all tasks to the pool immediately, 
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

- https://superfastpython.com/processpoolexecutor-in-python/