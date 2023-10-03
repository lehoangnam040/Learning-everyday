# First things first: Theory

- an object is an `awaitable` object if it can be used in an `await` expression.
- 3 main types of `awaitable`: coroutine, Task, and Future
- coroutines:
  - coroutine function: an `async def` function
  - coroutine object: an object returned by calling a coroutine function
- task:
  - used to schedule coroutine concurrently
- Future:
  - a special low-level awaitable object that presents an "eventual result" of an asynchronous operation
  - normally, "no need" to create Future object at the application level

## Task code
- create_task:
  - wrap coroutine into a Task and schedule its execution
  - is executed in the loop return by `get_running_loop`, raise Error if no running loop
  - IMPORTANT NOTE: save reference of Task object, to avoid being garbage collected at any time
- cancel task:
  - Task can easily and safely be cancelled
  - will raise `CancelledError` and should be try...except
- TaskGroup:
  - context manager holding and wait for all tasks inside

# References:

- https://docs.python.org/3/library/asyncio-task.html