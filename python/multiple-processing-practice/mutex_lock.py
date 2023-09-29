from multiprocessing import Lock, Process
from time import sleep


def task(lock, i: int):

    for _ in range(2):
        if lock is not None:
            with lock:
                print(f"process {i} got lock, sleep")
                sleep(1)
        else:
            print(f"process {i} sleep")
            sleep(1)
    


if __name__ == '__main__':
    lock = Lock()

    # without lock
    # processes = [Process(target=task, args=(None, i)) for i in range(10)]
    # with lock
    processes = [Process(target=task, args=(lock, i)) for i in range(10)]
    for process in processes:
        process.start()
    for process in processes:
        process.join()