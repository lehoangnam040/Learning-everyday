from multiprocessing.shared_memory import SharedMemory
from multiprocessing import resource_tracker
import time
import sys

if __name__ == "__main__":
    i = sys.argv[1]

    if i == "1":
        sm = SharedMemory(name="namlh", create=True, size=100)
        for _ in range(10):
            time.sleep(2)
            print("----", bytes(sm.buf[:11]).decode())
        sm.close()
        sm.unlink()
    elif i == "2":
        sm1 = SharedMemory(name="namlh", create=False)
        resource_tracker.unregister(f"/{sm1.name}", "shared_memory")
        sm1.buf[:11] = b"hello world"
        sm1.close()
    elif i == "3":
        sm = SharedMemory(name="namlh")
        resource_tracker.unregister(f"/{sm.name}", "shared_memory")
        print("*****", bytes(sm.buf[:11]).decode())
        sm.close()
    elif i == "4":
        sm = SharedMemory(name="namlh", create=True, size=50)  # Error
