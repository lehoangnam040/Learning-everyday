# Binary Encoding

## Primative types

- keys and values have a type: integer, date or string. it can be serialized and deserialized in raw binary form
- numeric data types are represented as fixed-size values
- Using byte-order (Big-endian / Little-endian) for both encoding / decoding

## strings and variable-size data
- these data can be represented as a struct, with a number (size) repesenting the length of array, and "size" bytes: actual data.

## Bit-packed data: bool, enum, flag
- bool: only 1 bit 0 / 1 values. Using an entire byte for it is wasteful, and we often batch bool values together in groups of 8.
- enum: represented as integers, for often-repeated low-cardinality values
- flag: power-of-2 values for representing -> using bitwise to test


# General principles
- The file starts with fixed-size header and may end with fixed-size trailer, the rest of the file is split into pages
- since there're many complex data types in database, a lookup table contains information of these parts often written in header/trailer or in the separate file

# Page structure
- db system store data records in data / index files. these files are partitioned into fixed-size units call pages
- Page sizes usually range from 4 - 16 kb
- we need a page format:
  - store variable-size with minimal overhead
  - reclaim space occupied by the removed records
  - reference records in the page without regard to their exact location

# Slotted page
- it efficiently store variable-size records
- used by many database, ex: PostgreSQL
- organizing the page into a collection of cell and split out pointers and cells into 2 locations
- cells may differ in size and can hold arbitrary data
- it has a fixed-size header holds information about the page and cell
- solve the problems of page:
  - minimal overhead: only overhead is a pointer array holding offset to locations
  - space reclaimation: defragmenting and rewriting the page
  - dynamic layout: cells are referenced only by ID -> exact location is internal to the page
- deleting records can be done by nullifying / remove pointers 


## Cell Layout
- cells is combined into pages
- cell has 2 type:
  - key cell: 
    - pointer to the page
    - layout: [int] key_size | [int] page_id | [bytes] key
  - key-value cell: 
    - hold keys and data records
    - layout: [byte] flags | [int] key_size | [int] value_size | [bytes] key | [bytes] data_record

## Combining cells into slotted pages
- the layout of page
```
[header] [offset][offset][offset]...[free space] [cell][cell][cell]...
```

- append cells to right side, keep offsets (pointers) to the left side
- cells are laid out in insertion order, but offset are sorted to allow using binary search

## Managing variable-size data
- remove item from the page: 
  - remove pointer
  - mark cell as available in a in-memory `availability list` 
- insert new cell:
  - first check this `availability list`
  - can fit the cell using `first fit` or `best fit`
  - if cannot find enough consecutive bytes to fit new cell -> live cells are rewritten to defragment

# Versioning
- DB can be improved -> the file format can change -> need to find out which version
- Apache Cassandra is using version prefixes in filenames
- PostgreSQL stores version in `PG_VERSION` file
- version can be stored in the index file header

# Checksum
- file on disk may get damaged or corrupted -> need a way to identify problems -> using checksum and CRCs


# References

- [Database internals](https://www.databass.dev/) Chap 3