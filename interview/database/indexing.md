- When to use indexes
  - Frequently used queries with WHERE, JOIN, ORDER BY
  - Retrive small set of records
  - Fields with unique restrictions, such as .._id

- When NOT to use indexes
  - Very low cardinality. Ex: Gender
  - Too little data
  - Frequently updated columns. Ex: balance

- What are disadvantages of indexes? Answer: A & B
  - A. Slowing down write operations
  - B. Occupying physical space
  - C. It takes time to create and maintain indexes

- Why the value of secondary index point to the primary key value, 
not the disk address?
  - The disk address of records might be change during table operating, defragment

- Which ones use index. Answer: C
  - A. SELECT * FROM users WHERE name LIKE ‘%ronin’
  - B. SELECT * FROM users WHERE name LIKE ‘%ronin%’
  - C. SELECT * FROM users WHERE name LIKE ‘ronin%’

- Does this query `SELECT * FROM users WHERE length(name) = 6;` use index on `name` column?
  - No. Because index ONLY contains original value of `name`, not the value calculated by function `length`
  - Same with these queries:
```
SELECT * FROM users WHERE id + 1 = 10;
SELECT * FROM users WHERE id + 0 = 10 - 1;  
```

- Assume we have Composite index: (country, provine, name). Which one uses index? Answer: A and D Because order of columns in composite index matters, so we need country in query to use index
  - A. SELECT * FROM customers WHERE provine = ‘Texas’ AND country = ‘US’;
  - B. SELECT * FROM customers WHERE provine = ‘Texas’; 
  - C. SELECT * FROM customers WHERE name = ‘JANE’ AND provine = ‘Texas’;
  - D. SELECT * FROM customers WHERE country = ‘US’;

- 