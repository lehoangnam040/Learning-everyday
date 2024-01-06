from multiprocessing.shared_memory import SharedMemory
from multiprocessing import resource_tracker
import time
import sys

import cv2 as cv

print("Opening camera...")
cap = cv.VideoCapture(0)
cap.set(cv.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 720)


sm = SharedMemory(name="namlh", create=True, size=2764800)
try:
    while True:
        ret, img = cap.read()
        if not ret:
            break

        # write image
        start = time.perf_counter()
        sm.buf[:] = img.tobytes()
        stop = time.perf_counter()

        print("Writing Duration:", (stop - start) * 1000, "ms")
except KeyboardInterrupt:
    pass
print("Closing resources")
cap.release()
sm.close()
sm.unlink()