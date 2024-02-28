## AOF (Append Only File)

- there's a AOF buffer to record commands and then sync to disk
- cons 
  - too many logs -> slow to recover

## RDB (Redis database)

- there is a job to create RDB snapshot periodically and sync to disk

-> Redis use Hybrid mode, combine both AOF and RDB