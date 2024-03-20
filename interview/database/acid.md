- Explain ACID in an example of transfering money

  - Atomicity: money needs to be both removed from sender and added to receiver, or the transaction will be aborted
  - Consistency: there's a database constraint that an account balance cannot drop below 0. All upgrades to an account balance inside of a transaction must leave the account with a valid, non-negative balance, or the transaction is aborted
  - Isolation: There're 2 concurrent requests to transfer money from the same bank account. The final result of running these transfers concurrently should be the same as running the transfers sequentially
  - Durability: Consider a power failure immediately after a transaction committed. The database should still hold the updated information.

- Deadlock in transfering money
  - https://mbukowicz.github.io/databases/2020/05/03/simple-locking-use-cases-in-postgresql.html

| T1 | T2 |
| ---------------------------------------------------------------- | --- |  
| UPDATE accounts SET balance = balance - 100 WHERE owner = 'Bob'; | UPDATE accounts SET balance = balance - 300 WHERE owner = 'Alice'; |
| UPDATE accounts SET balance = balance + 100 WHERE owner = 'Alice'; | UPDATE accounts SET balance = balance + 300 WHERE owner = 'Bob'; |

- Solve this problem by ordering
always update 'Alice' first, then 'Bob' -> no deadlock

- Solve transfering money deadlock by `FOR UPDATE SKIP LOCKED`
adding this query on the beginning of two transactions -> one transaction would be aborted
- `SELECT * FROM accounts WHERE "owner" in ('Bob', 'Alice') FOR UPDATE SKIP LOCKED;`
-> not so good for performance

- Avoid deadlock in transaction? Listing question
  - keep transaction short, order
  - ...