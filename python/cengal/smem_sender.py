from cengal.hardware.memory.shared_memory import SharedMemory, wait_my_turn, FreeMemoryChunkNotFoundError, numpy_array_memory_size
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
shared_memory_size = max(1024*10, numpy_array_memory_size(shape, np.uint8) * 2) 
creator: SharedMemory = SharedMemory(shared_memory_name, True, shared_memory_size)

img = np.random.randint(0, 255, size=shape, dtype=np.uint8)

def main():
    print('Sender is waiting for consumers')
    creator.wait_consumer_ready()
    print('Sender is ready')
    try:
        while True:
            try:            
                with wait_my_turn(creator, periodic_sleep_time=None):
                    start = time.perf_counter()
                    x = img.tobytes()
                    creator.put_message(x)
                    stop = time.perf_counter()
                delta_time = stop - start
                print("Writing Duration:", delta_time * 1000, "ms")
                print("Speed:", 1 / delta_time, "puts/s")
            except FreeMemoryChunkNotFoundError as ex:
                raise
                # print("got FreeMemoryChunkNotFoundError", ex)
    except KeyboardInterrupt:
        print("Keyboard interrupt")
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