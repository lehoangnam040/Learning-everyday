# Architecture

## Master-Slave

- data is written to master, then replicated to slave asynchronously
- pros
  - scalable for reads
- cons
  - data inconsistency
  - `failover`: promote slave algo?

## Sentinel

- add odd number of sentinel nodes to monitor master and slave
- sentinel node acts as a role of service discovery
- pros:
  - solve `failover`: sentinels elect 1 node as leader to promote a slave
- cons:
  - not scale for writes

## Cluster

- distribute data on different servers
- pros
  - solve `failover`
  - scale for read/write
  - solve write only on master
- cons
  - data inconsistency
  - more servers, more cost