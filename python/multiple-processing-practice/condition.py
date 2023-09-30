from multiprocessing import Condition, Process
import time

def task(condition):
    time.sleep(3)
    print("child process is about to send notify", flush=True)
    with condition:
        condition.notify()
    time.sleep(3)
    print("child process done")


def worker(condition, number):
    print(f"process {number} is waiting", flush=True)
    with condition:
        print(f"process {number} with condition", flush=True)
        condition.wait()
    print(f"process {number} recv notify")
    time.sleep(3)
    print(f"process {number} done", flush=True)

def worker_chain(condition, number):
    print(f"process {number} is waiting", flush=True)
    with condition:
        print(f"process {number} with condition", flush=True)
        condition.wait()
        print(f"process {number} nofity to wake up other", flush=True)
        condition.notify(1)
    print(f"process {number} recv notify, wakeup")

if __name__ == '__main__':
    condition = Condition()
    p = Process(target=task, args=(condition, ))
    with condition:
        p.start()
        condition.wait()
    print("Main process done")

    print("---------------- Next example of notify all")
    processes = [Process(target=worker, args=(condition, i)) for i in range(5)]

    for p in processes:
        p.start()
    time.sleep(3)
    with condition:
        condition.notify_all()
    print("after notify, wait all child process to be done")
    for p in processes:
        p.join()

    print("------ Next example of chain notification")
    processes = [Process(target=worker_chain, args=(condition, i)) for i in range(5)]
    for p in processes:
        p.start()
    time.sleep(2)
    with condition:
        condition.notify(1)
    print("after notify, wait all child process to be done")
    for p in processes:
        p.join()
