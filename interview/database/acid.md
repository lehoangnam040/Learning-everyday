- Explain ACID in an example of transfering money

  - Atomicity: money needs to be both removed from sender and added to receiver, or the transaction will be aborted
  - Consistency: there's a database constraint that an account balance cannot drop below 0. All upgrades to an account balance inside of a transaction must leave the account with a valid, non-negative balance, or the transaction is aborted
  - Isolation: There're 2 concurrent requests to transfer money from the same bank account. The final result of running these transfers concurrently should be the same as running the transfers sequentially
  - Durability: Consider a power failure immediately after a transaction committed. The database should still hold the updated information.
