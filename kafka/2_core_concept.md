
## architecture
- broker:
  - a kafka cluster can have multiple brokers
  - responsible for persisting and serving messages
- zookeeper:
  - manage brokers and overall status of broker
  - will be removed in kafka 4.0
  
## topic & partition
- topic is a stream of messages/events -> split into a group of partitions

- a partition is a totally ordered, unbounded queue of messages
  - order queue: read message in FIFO order
  - unbounded: no finish point, messages will continuously put into queue

## offset
- offset is an unique ID of each message in a partition
- offset is defined after a record is written to a partition
- offset is auto inc from 0
- fast lookup: O(1)

## record
- record is aka a message / event
- record is immutable
- 6 attrs:
  - key: 
    - optional, non-unique
    - grouping related records
    - free form (string / array of bytes)
  - value:
    - describes an event
    - nullable
    - free form
  - header: set of free-form K-V that is metadata of this record
  - partition: which partition this record in
  - offset: ID of this record
  - timestamp: milisecs-precise timestamp set by broker when this record is appended to the partition

## producer
- which create messages and write to topics
- need Kafka SDK to implement a producer
- partition: can be explicit specified in this producer
- if no partition specified and `key != null` -> partition = murmur2(bytes(key)) % `num_partition` 
  -> same key always go to same partition
  -> but when `num_partition` changed, later key can go different partition
- if `key == null` -> round-robin OR `Sticky Paritioner`

## consumer
- which read messages from topics
- using pull/poll
- it does NOT remove messages from topics
- need Kafka SDK to implement a consumer
- `consumer-group`
  - is a load-balance mechanism -> distributing partitions approximately evenly to consumers within
  - every consumer need to be in a `consumer-group`
  - when new consumer join group -> rebalance is triggered
  - rule:
    - 1 partition is assigned to at MOST 1 consumer
    - 1 consumer can consumer MORE than 1 partition
    - X consumers > Y partitions -> (X-Y) consumers in idle mode -> for backup purposes

# replication
- A replica is a copy of a partition
- Replicas are distributed across brokers