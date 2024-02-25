
## Pessimistic vs Optimistic
- handle read/write data with multi-transaction

### Pessimistic Lock

- transaction T1 start and modify data, it acquire lock -> update data -> release lock
- other transactions have to wait until T1 finish
- Pros:
  - data integrity
- Cons:
  - concurrency bottlenecks
  - potential deadlock

### Optimistic Lock
- No lock, allow conflict to occur, but need to detect, resolve it at write time
- how:
  - all transactions can fetch data with current version, without blocking
  - update data with new version
  - commit transaction: acquire lock -> compare version == current version -> update and release lock if success or update failed
- implement:
  - time-based update detection: not recommend
  - new version column
- pros:
  - reduce lock -> higher concurrency
  - avoid deadlock
  - do not affect others
- cons:
  - risk of conflict
  - complex conflict resolution: retry in application when failed, need correct WHERE condition while acquire lock and update

## Exclusive lock vs Share lock
- based on operation-level
  - Share (Read): allow to read but lock to write
  - Exclusive (Write): lock on both read / write

|   | Shared lock | Exclusive Lock   |
|---|---|---|
| Shared lock  | [v]  |  [x] |
| Exclusive Lock  | [x] | [x] |


Example:
- T1 locks row 1 for read, T2 can lock row 1 for read
- T1 lock row 1 for read, T2 can NOT lock row 1 for write
- T1 lock row 1 for write, T2 can NOT lock row 1 for write / read