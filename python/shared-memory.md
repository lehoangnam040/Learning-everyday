
# First things first: Theory

- allocation and management of shared memory to be accessed by 1 or more processes
- refers to "System V Style" shared memory blocks, NOT "distributed shared memory"
- permits processes to potentially read and write to a common region of volatile memory
- provide significant performance compared to sharing data via disk or socket requiring serialization / deserialization and copying of data


# Code

- When create `SharedMemory(name="abc")` object, on Linux, it will create file `/dev/shm/abc`
- If run on different program by `python ...`, on child process need to add `resource_tracker.unregister(f"/{sm.name}", "shared_memory")` to avoid resource_tracker auto delete `/dev/shm/abc` -> created process failed


# References

- https://docs.python.org/3/library/multiprocessing.shared_memory.html
- https://mingze-gao.com/posts/python-shared-memory-in-multiprocessing/