from multiprocessing import Event, Process
import time

def task(event, n):
    print(f"process {n} running")
    event.wait()
    print(f"process {n} right after event was set")
    time.sleep(3)
    print(f"process {n} closing")


if __name__ == '__main__':
    event = Event()

    processes = [Process(target=task, args=(event, i)) for i in range(10)]
    for p in processes:
        p.start()
    time.sleep(2)
    print("set event")
    event.set()
    for p in processes:
        p.join()