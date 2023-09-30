from multiprocessing import Process, Semaphore
import time

def task(semaphore, n):

    with semaphore:
        print(f"process {n} running")
        time.sleep(3)
        print(f"process {n} closing")


if __name__ == '__main__':
    semaphore = Semaphore(3)

    processes = [Process(target=task, args=(semaphore, i)) for i in range(10)]
    for p in processes:
        p.start()
    # Only 3 process can be run on the same time
    for p in processes:
        p.join()