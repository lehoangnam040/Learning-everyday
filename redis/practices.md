## String
- SDS (Simple Dynamic String)
- Applications:
  - cache JSOn
  - count
  - share sessions
  - distributed lock

## List
- Applications
  - message queue
- limit
  - max length is 2^32-1
  - no support multiple consumer
  - weak order preservation

## Hash
- Applications
  - cache objects
  - shopping cart
  - RediSearch

## Set
- Applications
  - deduplication of data
  - likes, common followers

## SortedSet (ZSET)
- Applications
  - leaderboard
  - sorting
