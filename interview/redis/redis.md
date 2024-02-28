- Why is Redis so fast?
  - in-memory
  - single thread model:
    - avoid multi-thread context switching
    - avoid locks or other synchronization mechanisms
  - multiplexing: 1 thread processes multiple IO streams
  - efficient data structure for different purposes

- Data structure of redis
  - hash table -> quick search O(1)

- expiration delete strategies
  - passive way: delete key when access it and check expire -> memory wasted
  - active way: periodic job (`activeExpireCycle`) to check and algo to delete
  -> redis combine both