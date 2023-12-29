## Logical architect

- Database cluster: include many databases
- Database: include many schemas
- Schema: include many objects
- Objects
  - Table
  - Index
  - Trigger
  - ...

All instaces (cluster, db, schema, ...) is managed by OID

## Physical architect

- Base directory for database cluster, all sub-folder are included inside here
  - Connection configuration files
    - `pg_hba.conf` : host-based authentication
    - `pg_ident.conf` : mapping file
  - Basic information files
    - `PG_VERSION`
    - `current_logfiles`
    - postmaster
      - `postmaster.opts`
      - `postmaster.pid`
  - Parameter files
    - `postgresql.conf` : configurations saved here
    - `postgresql.auto.conf` : using `ALTER SYSTEM` to change config
  - Sub-dir `base` :
    - many sub-dir corressponding to databases named with OID
  - Sub-dir `global` :
    - common table with OID using globally in database cluster
  - Sub-dir `pg_wal` :
    - store write-ahead-log segment files
- Table space
  - `pg_default` : other objects
  - `pg_global` : global / system objects

- Example in postgres 14 created by docker
```
root@2dc3e618908c:~# env | grep PGDATA
PGDATA=/var/lib/postgresql/data
root@2dc3e618908c:~# cd $PGDATA/
root@2dc3e618908c:/var/lib/postgresql/data# ls
base	      pg_dynshmem    pg_logical    pg_replslot	 pg_stat      pg_tblspc    pg_wal		 postgresql.conf
global	      pg_hba.conf    pg_multixact  pg_serial	 pg_stat_tmp  pg_twophase  pg_xact		 postmaster.opts
pg_commit_ts  pg_ident.conf  pg_notify	   pg_snapshots  pg_subtrans  PG_VERSION   postgresql.auto.conf  postmaster.pid
```

## References
- https://www.youtube.com/watch?v=OUlLQK_gN8k&t=516s (Vietnamese)