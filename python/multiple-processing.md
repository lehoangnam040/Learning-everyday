

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

- Using `multiprocess.Lock`

## Share state between processes

- Shared Memory: 
  - `from multiprocessing import Value, Array, sharedctypes`
  - process and thread-safe
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