- Ways to paginate in Postgres?
  https://www.citusdata.com/blog/2016/03/30/five-ways-to-paginate/
  - limit-offset: SELECT ... FROM ... LIMIT x OFFSET y;
  - cursor:
  ```
  BEGIN;

    DECLARE cursor_name CURSOR FOR SELECT ...;

    FETCH x FROM cursor_name;
    ..
    FETCH x FROM cursor_name;

  COMMIT;
  ```
  - keyset pagination
  ```
  CREATE INDEX n_idx ON tbl USING btree (n);

  SELECT * FROM tbl WHERE n > last_cursor ORDER BY n ASC LIMIT x;
  ```
  - clustered TID scan: choose return pages which correspond directly with DB pages on disk. Using secret column called ctid
  ```
  # physically reorder table by index and clustering
  CREATE INDEX n_idx ON tbl USING btree (n);
  CLUSTER tbl USING n_idx;

  # from now, it can be periodically re-clustered again through LOCK table 
  
  total number of pages: 
  SELECT pg_relation_size('tbl') / current_setting('block_size')::int;

  ```
  - keyset with estimated bookmarks
  ```
    WITH bookmark AS (
        SELECT (histogram_bounds::text::int[])[((page * per_page) / 100000)+1] AS start,
            (histogram_bounds::text::int[])[((page * per_page) / 100000)+2] AS stop
        FROM pg_stats
        WHERE tablename = 'tbl'
        AND attname = 'n'
        LIMIT 1
    )
    SELECT *
    FROM tbl
    WHERE n >= (select start from bookmark)
    AND n < (select stop from bookmark)
    ORDER BY n ASC
    LIMIT per_page
    OFFSET ((page * per_page) % 100000);
  ```