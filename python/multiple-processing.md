

# First things first: Theory

- Python process is a process in OS refers to a computer program
- A process is instance of Python interpreter
- A process always have at least 1 thread, called main thread

## Start methods

- The OS controls how new processes are created
- multiprocessing supports 3 ways to start a process
  - spawn: child process only inherit some neccessary resouces. slow compare to others. default on Windows / MacOS, available on Unix / Window
  - fork: child process inherit all resources, identical to parent process. Default on Unix, available on Unix only
  - forkserver: a server process is started. Then, parent process connects to this server and requests that it fork a new process. Fork server is single threaded.
- can change start methods by `multiprocessing.set_start_method`

## Exchanging objects between processes

- Queue
  - queues are thread and process safe

- Pipe
  - returns pair of connection objects connected by a pipe
  - Can be duplex (two-way) or unidirectional (one-way) 

## Synchronization

| Technique | usage |
| --------- | ------- |
| Lock      | called mutex. can be acquired by only 1 process at a time. other process will be blocked when trying to acquire
| RLock     | extend of mutex, can be acquired more than once by the same process | 
| Event     | primitive condition that wait on every process for the nofication by calling `set()`
| Condition | extend of mutex combine with Event, with wait for the notification from other process. while waiting, it release the lock for other process to acquire. But can set notify(number) or notify_all(), while Event `set()` same as `notify_all()` 
| Semaphore | extend of mutex, allow limit number of process to acquire a lock of critical section
| BoundedSemaphore | same as Semaphore, but cannot call `release()` more than limit, safer but we usually use `with semaphore` so IMO it isn't a big problem
| Barrier | primitive synchronization. Opposite to semaphore, `Barrier(N)`` makes all process run first and when number of process reach the number `N`, barrier will be released for them and wait for other N processes to reach barrier

## Share state between processes

- Shared Memory Data types: 
  - `from multiprocessing import sharedctypes`
  - `Value, Array` are process and thread-safe
  - `RawValue | RawArray` don't use mutex -> aren't process-safe
- Server process:
  - `from multiprocessing import Manager`
  - `Manager()` instance support many types that can be shared -> more flexible
  - slower than shared memory

## Pool of workers

- `from multiprocessing import Pool`
- can control number of simultaneously process


# References

- https://docs.python.org/3/library/multiprocessing.html
- https://superfastpython.com/multiprocessing-in-python/
- 