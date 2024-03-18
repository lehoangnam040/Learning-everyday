https://www.postgresql.org/docs/current/transaction-iso.html

## Read uncommitted
- Not allowed in Postgres

## Repeatable Read
- prevent "Phantom read" due to using `snapshot isolation`

## Serializable
- prevent "Serialization Anomaly" problem

Ref:
- https://mbukowicz.github.io/databases/2020/05/01/snapshot-isolation-in-postgresql.html