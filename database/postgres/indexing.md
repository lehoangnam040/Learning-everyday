# Hash index
- Cannot composite index with hash index.
  - Hash index's only suitable for equal comparision, only fit with all columns in the composite index are using equal comparision
  - postgres uses [32-bit](https://www.postgresql.org/docs/current/indexes-types.html#INDEXES-TYPES-HASH) to store hash -> about 4M unique values. So when using composite index, the number of unique values is decrease -> not well-suited for hash-index