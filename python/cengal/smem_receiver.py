from cengal.hardware.memory.shared_memory import SharedMemory, wait_my_turn, numpy_array_memory_size
import numpy as np
import time

shared_memory_name: str = 'namlh'
shape = (100, 100, 3)
shared_memory_size = max(1024*10, numpy_array_memory_size(shape, np.uint8) * 2) 
consumer: SharedMemory = SharedMemory(shared_memory_name, False, shared_memory_size)
try:
    import _posixshmem
    from multiprocessing import resource_tracker
    shm_name = f'/{shared_memory_name}'
    resource_tracker.unregister(shm_name, "shared_memory")
except FileNotFoundError:
    pass


def main():
    print('Consumer is ready')
    need_to_stop = False
    while not need_to_stop:
        
        with wait_my_turn(consumer, periodic_sleep_time=None):
            start = time.perf_counter()
            while consumer.has_messages():
                obj, obj_offset = consumer.take_message_2()
                if obj is None:
                    need_to_stop = True
                else:
                    _ = np.frombuffer(obj, dtype=np.uint8).reshape(shape)
                if obj_offset:
                    consumer.destroy_object(obj_offset)
                if need_to_stop:
                    break
            stop = time.perf_counter()
            print("Read Duration:", (stop - start) * 1000, "ms")

if '__main__' == __name__:
    main()