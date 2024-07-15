## ACK
- it's a signal sent from receiver to sender indicating that message has been delivered successfully
- ACK = 0
  - producers require no ACK from the broker
  - fire and forget
  - pros: most performance
  - cons:
    - message might be lost
    - no offset in the metadata
  - usecases:
    - metrics from IoT devices
    - non-essential logs
- ACK = 1
  - producers require ACK from the leader only
  - pros:
    - high performance
    - offset in the metadata
  - cons:
    - messages might be lost
  - usecases:
    - user tracking activity
    - tracking clicks, views, ...
- ACK = -1 (all)
  - producers will wait until leader gathered ACKs from ALL in-sync replicas (ISRs)
  - replication here is synchronous
  - pros:
    - strong durability of messages
  - cons:
    - high latency
  - usecases:
    - financial activity
    - order, payment


## Retry