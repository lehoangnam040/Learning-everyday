from cengal.hardware.memory.shared_memory import SharedMemory, wait_my_turn
import numpy as np
import time

shared_memory_name: str = 'namlh'

# `multiprocessing.SharedMemory` requires this cleanup in order to handle the case 
# when the previous run of the program was terminated unexpectedly:
try:
    import _posixshmem
    from multiprocessing import resource_tracker
    shm_name = f'/{shared_memory_name}'
    _posixshmem.shm_unlink(shm_name)
    resource_tracker.unregister(shm_name, "shared_memory")
except FileNotFoundError:
    pass

shape = (100, 100, 3)
shared_memory_size = int(np.prod(shape))
print(shared_memory_size)
creator: SharedMemory = SharedMemory(shared_memory_name, True, shared_memory_size)

img = np.random.rand(*shape).astype(np.uint8)

def main():
    print('Sender is waiting for consumers')
    creator.wait_consumer_ready()
    print('Sender is ready')
    try:
        while True:
            start = time.perf_counter()
            with wait_my_turn(creator, periodic_sleep_time=None):
                x = img.tobytes()
                print(type(x), len(x))
                creator.put_message(x)
            stop = time.perf_counter()
            print("Writing Duration:", (stop - start) * 1000, "ms")
    except KeyboardInterrupt:
        pass
    finally:
        with wait_my_turn(creator, periodic_sleep_time=None):
            creator.put_message(None)

if '__main__' == __name__:
    try:
        main()
    # except Exception as err:
    #     print(err)
    finally:
        creator._shared_memory.close()
        creator._shared_memory.unlink()