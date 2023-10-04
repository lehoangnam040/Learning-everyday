# First things first: Theory

- `asyncio.run`:
  - run passed coroutine, manage event loop, and closing executor
  - cann be called when another event loop is running in the same thread
- `asyncio.Runner`:
  - context manager simplifies multiple async function calls in the same context
- handling SIGINT by Ctrl-C:
  - asyncio installs custom SIGINT handler before user code
  - this custom signal handler cancels main task of asyncio -> after cancelled, asyncio raise `KeyboardInterrupt`
  - user now can handle it