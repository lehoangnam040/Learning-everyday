from multiprocessing.shared_memory import SharedMemory
from multiprocessing import resource_tracker
import time
import sys
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

sm = SharedMemory(name="namlh")
resource_tracker.unregister(f"/{sm.name}", "shared_memory")
shape = (720, 1280, 3)
img = np.zeros(shape)

im = plt.imshow(img)

while True:
    # read image
    try:
        start = time.perf_counter()
        img = np.frombuffer(sm.buf[:], dtype=np.uint8).reshape(shape)
        stop = time.perf_counter()

        print("Reading Duration:", (stop - start) * 1000, "ms")
        im.set_data(img)
        plt.pause(0.01)

        # time.sleep(2)
        
        # cv.imwrite(f"{stop}.png" , img)
    except:
        break
    
print("*****", bytes(sm.buf[:11]).decode())
sm.close()
plt.show()
