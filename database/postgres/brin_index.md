## General
- What?
  - BRIN is an specialized index
  - "natural correlation" data is data with timestamp continuously adding new rows
    - log table
    - GPS track points table
    - IoT sensor measurements table
- Why?
  - BRIN offer extremely low insert costs and extremely small index sizes for "natural correlation" data
- How?
  - data in Pg tables are arranged on disk with equal-sized "pages" = 8kb
  - since each page holds multiple rows -> we can determine min/max value of a column in a page -> when searching for a value, we can skip a page based on min/max of that page
  - BRIN index is a small table that contains range of values associate with range of pages
    - build BRIN index fast since it just requires a single scan on a table
    - BRIN index is small since it only has range of pages and min/max of values


## Ref:
https://www.crunchydata.com/blog/postgres-indexing-when-does-brin-win