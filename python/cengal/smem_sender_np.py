from cengal.hardware.memory.shared_memory import (
    SharedMemory, 
    wait_my_turn, 
    numpy_array_made_from_pointer_memory_size,
    make_numpy_array_from_obj_offset,
)
import ctypes
import numpy as np
import time
import cv2 as cv

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

shape = (720, 1280, 3)
shared_memory_size = max(1024*10, numpy_array_made_from_pointer_memory_size(shape, ctypes.c_uint8) * 2)
creator: SharedMemory = SharedMemory(shared_memory_name, True, shared_memory_size)
cap = cv.VideoCapture(0)
cap.set(cv.CAP_PROP_FRAME_WIDTH, shape[1])
cap.set(cv.CAP_PROP_FRAME_HEIGHT, shape[0])

def main():
    print('Sender is waiting for consumers')
    creator.wait_consumer_ready()
    print('Sender is ready')
    try:
        holder: bytes = b'\x00' * numpy_array_made_from_pointer_memory_size(shape, ctypes.c_uint8)
        with wait_my_turn(creator):
            _, holder_offset = creator.put_message_2(holder)
            np_arr: np.ndarray = make_numpy_array_from_obj_offset(creator, holder_offset, shape, ctypes.c_uint8)
            np_arr.fill(0.0)
        while True:
            with wait_my_turn(creator):
                ret, img = cap.read()
                if not ret:
                    break
                start = time.perf_counter()
                np_arr[:,:,:] = img
                stop = time.perf_counter()
            delta_time = stop - start
            print("Writing Duration:", delta_time * 1000, "ms")
            print("Speed:", 1 / delta_time, "puts/s")
    except KeyboardInterrupt:
        print("Keyboard interrupt")
    finally:
        cap.release()
        with wait_my_turn(creator):
            creator.put_message(None)

if '__main__' == __name__:
    try:
        main()
    # except Exception as err:
    #     print(err)
    finally:
        creator._shared_memory.close()
        creator._shared_memory.unlink()