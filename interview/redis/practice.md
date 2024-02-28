- delay queue for context: cancel order within a duration of time?
  - using ZSET with key is order and score is timestamp

- distributed lock
  - use [SETNX](https://redis.io/docs/manual/patterns/distributed-locks/) in single instance
