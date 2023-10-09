
- We can have concurrency within 1 process and 1 thread
- Do this by exploiting the fact that, at the system level, I/O operations can be completed concurrently

# Socket

- socket is a low-level abstraction for sending / receiving data over a network
- write bytes to socket -> bytes is sent to a remote address
- then wait for bytes is response back to our socket
- at OS level, sockets can operate in non-blocking mode
  - when write bytes to socket, we can just fire and forget it to do another tasks
  - later, OS tell us that we received bytes and deal with it
- In the background, this is performed by a few different notification systems, depending on OS
  - kqueue by FreeBSD & MacOS
  - epoll by Linux
  - IOCP (I/O completion port) by Windows

# Single thread concurrency

- in this mode, we have only 1 thread executing code at any given time
- When hit I/O operation, we leave it to our OS notification systems to keep track
- then our thread is free to keep running other tasks
- when above I/O operation finishes, we wake up the task that was waiting for the result and then continue to run
- keep track by event loop

# Event loop
- a common design pattern in many concurrency systems
- basic of an event loop is a queue that holds a list of events / messages
- then loop the queue forever, processing messages one at a time as they come into the queue
- 