from time import sleep
from multiprocessing import RLock, Process, Lock



def report(lock, i):
    with lock:
        print(f"process {i} after sleep, reported")

def task(lock, i):

    with lock:
        print(f"process {i} got lock to sleep")
        sleep(2)
        report(lock, i)


if __name__ == '__main__':
    # allow a process to acquire a lock more than 1
    lock = RLock()

    processes = [Process(target=task, args=(lock, i)) for i in range(10)]
    for process in processes:
        process.start()
    for process in processes:
        process.join()  