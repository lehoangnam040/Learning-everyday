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

## Hash index
- Use hash function to map keys to specific locations
- Well-suited for equal comparisions 
- Not well-suited for range queries, sorting