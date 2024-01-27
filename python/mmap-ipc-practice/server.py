"""
Continuously read images from webcam and write them to a memory-mapped file.
"""
import mmap
import time

import cv2 as cv

print("Opening camera...")
cap = cv.VideoCapture(0)
cap.set(cv.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 720)

mm = None
try:
    while True:
        ret, img = cap.read()
        if not ret:
            break
        if mm is None:
            mm = mmap.mmap(-1, img.size)

        # write image
        start = time.perf_counter()
        buf = img.tobytes()
        mm.seek(0)
        mm.write(buf)
        mm.flush()
        stop = time.perf_counter()
        

        print("Writing Duration:", (stop - start) * 1000, "ms")
        break
except KeyboardInterrupt:
    pass
print("Closing resources")
cap.release()
mm.close()