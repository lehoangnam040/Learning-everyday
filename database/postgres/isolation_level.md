https://www.postgresql.org/docs/current/transaction-iso.html

## Read uncommitted
- Not allowed in Postgres

## Repeatable Read
- prevent "Phantom read" due to using `snapshot isolation`

## Serializable
- prevent "Serialization Anomaly" problem