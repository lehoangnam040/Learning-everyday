from multiprocessing.shared_memory import SharedMemory
from multiprocessing import resource_tracker
import time
import numpy as np
import cv2

sm = SharedMemory(name="namlh")
resource_tracker.unregister(f"/{sm.name}", "shared_memory")
shape = (720, 1280, 3)
# shape = (3000, 4000, 3)


while True:
    # read image
    try:
        start = time.perf_counter()
        img = np.frombuffer(sm.buf[:], dtype=np.uint8).reshape(shape)
        stop = time.perf_counter()

        print("Reading Duration:", (stop - start) * 1000, "ms", img.shape)
        cv2.imshow("video", img)
        if cv2.waitKey(10) & 0xFF == ord('q'): 
            break
    except:
        break

sm.close()
cv2.destroyAllWindows()