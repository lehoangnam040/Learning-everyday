# First things first: Theory
- allow sending / receiving data without using callbacks or low-level protocols and transports

- coroutine `asyncio.open_connection`
  - establish a network connection and return a pair of `reader / writer` objects
- coroutine `asyncio.start_server`
  - start a socket server
  - `client_connected_cb` calback is called and pass `reader / writer` as pair of arguments
  - `client_connected_cb` will be scheduled as Task
- coroutine `asyncio.open_unix_connection`
  - establish a "Unix spcket" connection and return a pair of `reader / writer` objects
- coroutine `asyncio.start_unix_server`
  - start a "Unix" socket server

# References

- https://docs.python.org/3/library/asyncio-stream.html