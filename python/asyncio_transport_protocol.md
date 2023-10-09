# First things first: Theory
- Transport and Protocol are used by low-level event loop API
- They use callback-based programming style and enable high-performance
- should NOT be used in high-level asyncio applications
- Transport
  - concerned with how bytes are transmitted
  - is an abstraction for a socket
- Protocol
  - determines which bytes to transmit
  - is an abstraction for an application

# References:
- https://docs.python.org/3/library/asyncio-protocol.html