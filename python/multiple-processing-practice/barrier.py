from multiprocessing import Barrier, Process
import time


def report():
    print("barrier triggered action")

def task(barrier, n):

    time.sleep(2)
    print(f"process {n} wake up")
    barrier.wait()
    print(f"process {n} pass barrier")

if __name__ == '__main__':
    barrier = Barrier(5, action=report)
    processes = [Process(target=task, args=(barrier, i)) for i in range(15)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()