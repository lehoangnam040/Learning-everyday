# First things first: Theory

- similar to `threading` modules
- but not thread-safe
- do not accept `timeout` argument
- using `async with ...`

| Technique | usage |
| --------- | ------- |
| Lock      | called mutex. can be acquired by only 1 asyncio tasks at a time. other tasks will be blocked when trying to acquire
| RLock     | extend of mutex, can be acquired more than once by the same tasks | 
| Event     | primitive condition that wait on every tasks for the nofication by calling `set()`
| Condition | extend of mutex combine with Event, with wait for the notification from other tasks. while waiting, it release the lock for other tasks to acquire. But can set notify(number) or notify_all(), while Event `set()` same as `notify_all()` 
| Semaphore | extend of mutex, allow limit number of tasks to acquire a lock of critical section
| BoundedSemaphore | same as Semaphore, but cannot call `release()` more than limit, safer but we usually use `with semaphore` so IMO it isn't a big problem
| Barrier | primitive synchronization. Opposite to semaphore, `Barrier(N)`` makes all tasks run first and when number of tasks reach the number `N`, barrier will be released for them and wait for other N tasks to reach barrier


# References:
- https://docs.python.org/3/library/asyncio-sync.html