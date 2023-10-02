# First things first: Theory
- `contextvars` is a variable that can be defined per thread / per coroutine
- it's distinct per context
- each concurrent thread/coroutine may read / write its own values to the `contextvars`, which is isolated automatically from other concurrent tasks
- it's different with thread local storage
- from python 3.7

# References

- https://docs.python.org/3/library/contextvars.html
- https://superfastpython.com/thread-context-variables-in-python/
