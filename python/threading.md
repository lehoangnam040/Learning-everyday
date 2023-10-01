

# First things first: Theory

- `threading` interfaces on top of low level `_thread` module
- represent native thread provided by the underlying OS: POSIX threads on Linux and Windows thread on Window
- Python thread = OS thread + Python thread state
- fully managed by the host OS
- Thread are components of a process
- There can be multiple threads in a process, they share the same memory

## Thread scheduling
- C Python does NOT have a thread scheduler
- All thread scheduling is left to the host OS

## Synchronization

| Technique | usage |
| --------- | ------- |
| Lock      | called mutex. can be acquired by only 1 thread at a time. other thread will be blocked when trying to acquire
| RLock     | extend of mutex, can be acquired more than once by the same thread | 
| Event     | primitive condition that wait on every thread for the nofication by calling `set()`
| Condition | extend of mutex combine with Event, with wait for the notification from other thread. while waiting, it release the lock for other thread to acquire. But can set notify(number) or notify_all(), while Event `set()` same as `notify_all()` 
| Semaphore | extend of mutex, allow limit number of thread to acquire a lock of critical section
| BoundedSemaphore | same as Semaphore, but cannot call `release()` more than limit, safer but we usually use `with semaphore` so IMO it isn't a big problem
| Barrier | primitive synchronization. Opposite to semaphore, `Barrier(N)`` makes all thread run first and when number of thread reach the number `N`, barrier will be released for them and wait for other N threads to reach barrier

## Blocking call

- OS block current thread to do context switch to other thread
- Concurrency primitives: lock, condition, semaphore, event, barrier
- I/O blocking
- sleep


# References

- https://docs.python.org/3/library/multiprocessing.html
- https://superfastpython.com/multiprocessing-in-python/
- 