
- Redis propose an algo called `Redlock` to implement DLM (Distributed Lock Manger)
- DLM is how we distributed a lock in many redis instances to ensure the lock working


## Requirements
- `safety`: mutual exclusion. At any given moment, only 1 client hold the lock
- `liveness A`: deadlock free. eventually a lock is free to acquire, even if client that currently locked crashs or get partitioned
- `liveness B`: fault tolerance. client are able to acquire/release lock as long as majority of redis nodes are UP

## A case when Failover-based not enough
- Failover-based:
  - create a key in a node with TTL
  - if this node goes down then that key is replicated in another node
- But
  - it's NOT implement `safety` requirement
- Why
  - redis replication is asynchronous
- A race condition case:
  - client A lock in master
  - master crashes before replication
  - the replica node is promoted to be master
  - client B acquires that lock -> violate `safety`

## Redlock
- `N`(=5) redis master nodes, independently, not replication
- use method `SETNX` `PX` `expire`
- choose `timeout` << `expire`
- choose `lock_valid_time`
- steps:
  - 1. `ts_ms` = current timestamp in ms
  - 2. for i := range `N`:
    - acquire lock in node `i` in `timeout`
    - if node `i` crashs or no response:
      - continue
  - 3. `elapsed` = current timestamp in ms - `ts_ms`
    - if NOT success in `N//2` node or `elapsed` >= `lock_valid_time` -> acquire lock FAILED, go 5  ??
  - 4. `lock_valid_time` = `lock_valid_time` - `elapsed`    ??
  - 5. unlock in all instances

## Ref
- https://redis.io/docs/manual/patterns/distributed-locks/
- 