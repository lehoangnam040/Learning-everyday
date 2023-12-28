
# Definition

- A transaction is a "group of SQL queries" that are treated "atomically", as a single unit of work
- All (Success) or nothing: If one step is failed, transaction is falled back
- Syntax
```
BEGIN TRANSACTION
...
COMMIT  -- if success
ROLLBACK -- if failed
```

# ACID

- Atomicity: All or nothing
- Consistency: Always move from one valid state to another
- Isolation: executing transactions concurrently has same results as if executing sequentially
- Durability: Once commited, changes are permanent. Data won't be lost in DB crash

# Isolation levels
There're 4 types according to Standard SQL Transaction isolation levels 
- Read uncommitted
- Read committed
- Repeatable read
- Serializable

## Read uncommitted
- Transaction can view the results of uncommitted transactions
- Dirty read
- Good performance
- But Buggy, rarely used

## Read committed
- Transaction can only view the results of committed transactions
- Solve the "Dirty Read" problem
- Default level of most database
- Another problem: 
  - Non-repeatable read: read 2 different results of same query in a transaction, because another transaction committed make the data changed
  - Phantom read: read some more "phantom" rows of same query in a transaction, because another transaction committed add some records

## Repeatable read
- In a transaction, data are consistent among queries, despite another transactions committed
- Solve the "Non-repeatable read" problem
- Cannot prevent "Phantom read"

## Serializable
- Solve the "Phantom read" problem
- This is the highest isolation level
- In a nutshell, it places a lock on every row it reads
- But it decreases concurrency

# References
- https://aviator.co/blog/acid-transactions-postgresql-database/
