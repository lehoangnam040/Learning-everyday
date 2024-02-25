
# First things first: Theory

## GIL
- C Python have a thing call GIL, or Global Interpreter Lock
- GIL is a mutex that protects access to Python object, preventing threads from executing Python bytecodes at once
- GIL ensures that only 1 thread runs in the interpreter at once by gets exclusive access to the interpreter

## GIL behavior
- simple: a thread hold GIL when running
- however, it release GIL when blocking for I/O
- So, at that time, other "ready" threads get their chance to run
- it's basically a kind of "preemptive" multitasking
- In order to emulate concurrency of execution, the interpreter regularly tries to switch threads (see sys.setswitchinterval()).

## Scenario to describe GIL (on Unix)
- when start a program, main thread takes the GIL during initialization and hold the GIL
- other `threading.Thread()` object `start()`, it call C `pthread_create()`
- newly created thread executes `t_bootstrap()`, try to acquire the GIL to run its bytecode
- To acquire GIL, it first checks whether other thread holds the GIL
  - If No, it acquires the GIL immediately
  - Else, waits for a fixed time interval called (`switchinterval`)
  - If GIL not released during `switchinterval`, it sets the `eval_breaker` and `gil_drop_request` flags to tell GIL-holding thread to release GIL
  - when releasing GIL, one of waiting threads acquires the GIL, and it's up to OS to decide which thread is chosen

## Solution for this limitation
- Using multi-processing: each Python process gets its own Python interpreter so GIL won't be a problem -> this could become scaling bottleneck
- Using alternative Python interpreters without GIL (Jython, IronPython, PyPy): but comes with other limitations and not supported widely

## When using multithread to overcome limitations

- for blocking I/O task, to release GIL: r/w files, download / upload, querying DB, ...
- call external C code, to release GIL

# Practice by Code

```
# single threaded

COUNT = 50000000

def countdown(n):
    while n>0:
        n -= 1

start = time.time()
countdown(COUNT)
end = time.time()

```

```
# vs multi thread
t1 = Thread(target=countdown, args=(COUNT//2,))
t2 = Thread(target=countdown, args=(COUNT//2,))

start = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
end = time.time()
```

```
# single thread: 1.11s
# multi thread: 1.14s
-> almost same time to finish
```

# Reference

- https://docs.python.org/3/glossary.html#term-global-interpreter-lock
- https://superfastpython.com/gil-removed-from-python/
- https://realpython.com/intro-to-python-threading/
- https://www.dabeaz.com/python/UnderstandingGIL.pdf
- http://www.dabeaz.com/python/GIL.pdf
- https://tenthousandmeters.com/blog/python-behind-the-scenes-13-the-gil-and-its-effects-on-python-multithreading/