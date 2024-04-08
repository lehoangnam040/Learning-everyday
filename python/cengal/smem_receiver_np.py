from cengal.hardware.memory.shared_memory import (
    SharedMemory, 
    wait_my_turn, 
    numpy_array_made_from_pointer_memory_size,
    make_numpy_array_from_obj_offset,
)
import numpy as np
import time
import ctypes
import cv2

shared_memory_name: str = 'namlh'
shape = (720, 1280, 3)
shared_memory_size = max(1024*10, numpy_array_made_from_pointer_memory_size(shape, ctypes.c_uint8) * 2)
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
    cv2.namedWindow("video", cv2.WINDOW_AUTOSIZE)
    consumer.wait_for_messages()
    with wait_my_turn(consumer):
        _, holder_offset = consumer.take_message_2()
        np_arr: np.ndarray = make_numpy_array_from_obj_offset(consumer, holder_offset, shape, ctypes.c_uint8)
    
    need_to_stop = False
    try:
        while not need_to_stop:
            with wait_my_turn(consumer):
                # print("Read Duration:", (time.perf_counter() - start) * 1000, "ms")
                cv2.imshow("video", np_arr)
                # start = time.perf_counter()
            if cv2.waitKey(10) & 0xFF == ord('q'): 
                break
    except KeyboardInterrupt:
        pass
    finally:
        cv2.destroyAllWindows()

if '__main__' == __name__:
    main()