## Concept
- What?
  - GIN is Generalized Inverted Index, so-called inverted index
- When?
  - useful for composite values, with query search for element values within the composite items
- How?
  - it extracts values from a column, stores in a tree called GIN entry tree, with value and row ID
  - in case high-frequency values, row IDs are stored in a separate called posting tree
  - it also has a buffer called "fast update list", allow insert/update/delete values to be written into buffer first and merge into the tree

## Usecases
- Full-text search (tsvector)
- Array
- JSONB