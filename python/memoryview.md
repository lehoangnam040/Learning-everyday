# First things first: Theory

- allow Python code to access internal data of an object that supports the buffer protocol without copying
- `bytes` and `bytearray` support buffer protocol
- reduce the allocation of memory

# References

- https://docs.python.org/3/library/stdtypes.html#memoryview
- https://julien.danjou.info/high-performance-in-python-with-zero-copy-and-the-buffer-protocol/