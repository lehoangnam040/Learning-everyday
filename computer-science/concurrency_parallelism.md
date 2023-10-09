# Concurrency

- 2 tasks are happening concurrently means they are happening at the same time
- can have concurrency on CPU with only 1 core -> preemptive multitasking to switch between tasks

# Parallelism

- 2 tasks are happening parallel means they are also executing at the same time
- need CPU with multiple cores that can run 2 tasks together

# Multitasking

- Preemptive multitasking
  - let the OS decide how to switch between tasks, via a process called time slicing
  - when OS switches between work, we call it preempting
- Cooperative multitasking
  - instead of relying on the OS, the code of application will decide it.
- Benefit of cooperative multitasking
  - less resource intensive, no need context switching when OS switches between thread / process
  - granulatiry. we explicitly mark the areas that are the best for pausing and doing another tasks
- 