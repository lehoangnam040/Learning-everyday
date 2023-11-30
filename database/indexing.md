# Definitions

- WHAT: index is a data structure
- WHEN:
  - improves the speed of data retrieval operations
- HOW:
  - typically stored on disk
  - indexing on a column means creating "data structure" to hold values of that column and map (pointers) to the original record
- WHY:
  - Pros: improve reading speed
  - Cons: 
    - make update/insert/delete slower
    - consume more storage space

# Classification
- Data structure: B+ tree, Hash
- Physical storage: Clustered, Secondary
- Number of fields: Single-column, Composite
- Characteristics: Primary key, Unique, Prefix

# Data structure Indexes

## B+ tree
- All leaves are at the same level
- Pointers to records are stored ONLY at the leaf nodes
- All leaf nodes are linked in a linked list in sort order -> Efficient for range queries
- Non-leaf nodes ONLY contain keys and pointers to children nodes
- Insert/Delete/Search operations in O(logN)
- become imbalance overtime -> need to rebuild index
- My code: https://github.com/lehoangnam040/b-plus-tree

## Hash index
- Use hash function to map keys to specific locations
- Well-suited for equal comparisions 
- Not well-suited for range queries, sorting

# Physical Storage Index

## Clustered index
- is a type of index that determines the physical order of data in a table
- A table can have ONLY 1 clustered index
- By default, PK is used for clustered index
- Using B+ tree, leaf node stores actual data of table rows

## Non-clustered index
- Type of index isn't clustered index
- A table can have MULTIPLE non-clustered index
- Leaf node stores data that is PK value
- Access data involves AT LEAST 2 disk read. First one to access PK in clustered index and Second one to get actual data

# Number of columns

## Composite index

- is a multiple-column index
- the more columns are used, the more space are used


## Covering index

- is an index that contains all the columns in the SELECT ...
- could improve the performance significantly
- recommend: <= 5 columns