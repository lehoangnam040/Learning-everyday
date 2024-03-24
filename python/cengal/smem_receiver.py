from cengal.hardware.memory.shared_memory import SharedMemory, wait_my_turn
import numpy as np
import time

shared_memory_name: str = 'namlh'
shape = (100, 100, 3)
shared_memory_size = int(np.prod(shape))
consumer: SharedMemory = SharedMemory(shared_memory_name, False, shared_memory_size)
try:
    import _posixshmem
    from multiprocessing import resource_tracker
    shm_name = f'/{shared_memory_name}'
    resource_tracker.unregister(shm_name, "shared_memory")
except FileNotFoundError:
    pass

img = np.random.rand(*shape).astype(np.uint8)

def main():
    print('Consumer is ready')
    need_to_stop = False
    while not need_to_stop:
        start = time.perf_counter()
        with wait_my_turn(consumer, periodic_sleep_time=None):
            while consumer.has_messages():
                new_message = consumer.take_message()
                if new_message is None:
                    need_to_stop = True
                    break
                print(new_message)
                _ = np.frombuffer(new_message, dtype=np.uint8).reshape(shape)
        stop = time.perf_counter()
        print("Read Duration:", (stop - start) * 1000, "ms")

if '__main__' == __name__:
    main()