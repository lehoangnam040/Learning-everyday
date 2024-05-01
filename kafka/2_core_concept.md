
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