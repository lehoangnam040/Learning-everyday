
# First things first: Theory

- `ThreadPoolExecutor` is an `Executor` subclass, use pool of threads to execute call async
- deadlocks can occur if bugs in code
- exceptions in main thread must be caught and handled in order to signal threads to exit gracefully -> recommend this class should NOT be used for long-running tasks

# References

- https://superfastpython.com/threadpoolexecutor-in-python/