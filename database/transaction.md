
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


# References
- https://aviator.co/blog/acid-transactions-postgresql-database/
