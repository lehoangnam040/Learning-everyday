# Definitions
- storage engine or db engine is a software component of DBMS responsible for
  - storing     |
  - retrieving  |   data in memory / disk
  - managing    |
- Another, DBMS is application built on top of storage engine
- Typically, the storage engine has several components:
  - transaction manager: schedules transactions, ensure the consistent of DBMS
  - lock manager: locks DB objects for the running transactions, ensure data integrity
  - access methods (storage structures): manage access and organizing data on disk. include heap files and storage structures such as B-tree / LSM-tree
  - buffer manager: caches data pages in memory
  - recovery manager: maintains operation logs and restoring system state in case of a failure
-> transaction & lock manager are responsible for concurrency control

# Classification

## Memory vs Disk -Based
- In-memory DB store data primarily in memory and use disk for recovery and logging
- Disk-based DB hold most of the data on disk and use memory for caching or temporary storage

## Column vs Row -Oriented
- Row-based: storing values belonging to the same row together
- Column-based: storing values belonging to the same column together

- Row-based data layout
  - similar to tabular data representation. Ex: Excel
  - Each row are uniquely identified by the key
  - useful in case when we have to access data by row

- Column-based data layout
  - values for the same column are stored contiguously on disk
  - Ex: in historical stock market prices, price quotes are stored together
  - allow efficient queries by column
  - good fit for analytical, compute aggregate

## Data files and index files
- how the data is stored
- usually separates data files and index files
- data files: store data records
- index files: store metadata and use it to locate records in data files
- files are partitioned into pages, pages can be organized as sequences of records

- data files
  - index-organized tables (IOT): store in the index itself, with key in order, to improve range scans. Data entries hold data records.
  - heap-organized tables (heap files): place in write order, no additional work is required with pages are added, but require index structures.
  - hash-organized tables (hash files): store in buckets with hash value to improve lookup speed
- index files
  - map keys to locations in data files
  - index on PK is primary index, others are secondary indexes

# Common concepts of storage structures
- Buffering
  - whether or not it "chooses" to buffer data in memory before putting it on disk
- Mutability
  - whether or not it reads / updates / writes data at the same location in the file (mutable)
  - immutable structure means append-only
- Ordering
  - whether or not data records are stored in the key order in the pages on disk

# Reference

- [Database internals](https://www.databass.dev/) Chap 1