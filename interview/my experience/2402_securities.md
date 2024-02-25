### validate file type when do upload via presigned URL?
- it's client's responsibility to validate mime type
- but if not, then need a post process after s3 receive it

### design DB SQL or NoSQL to store list of directories / files with metadata + search with name on both directory / files
- System Design [here](../prev%20projects/1_robot_data_sync_system.md)
- For search with name on both directory / files: Need to build search text index to search on both

### advantages of using asyncio vs multiple threading?
- cooperative multi-task, much light-weight than OS threads
- support cancellation
- prevent context switching in OS level

### design a scale up/down approach for a topic when scale up on business time and scale down on night time?
...

### store session in 2 redis instance -> want to clear session on instance A -> trigger on instance B
...

### does Django Python apply Clean architect?

- Not really, since Django just supports only data access layer
- The controller layer is Django view and only http request -> Not fully apply Clean Architect
