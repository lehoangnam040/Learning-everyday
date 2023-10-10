# First things first: Theory
- a Future is a Python object that contains a single value we expect to get at some point in the future, but may not yet have
- Future objects are used to bridge low-level callback-based code with highlevel async/await code
- `await future` means "pause until the future has a value set, and once get a value, wake up and let us process it"
- recommend way to create Future object is through `loop.create_future()`
- 

# References:
- https://docs.python.org/3/library/asyncio-future.html