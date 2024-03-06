"""
Continuously read images from webcam and write them to a memory-mapped file.
"""
import mmap
import time
import numpy as np
import os
import cv2 as cv

print("Opening camera...")
cap = cv.VideoCapture(0)
cap.set(cv.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 720)
shape = (720, 1280, 3)
n = int(np.prod(shape))
fd = os.open('/tmp/mmaptest', os.O_CREAT | os.O_TRUNC | os.O_RDWR)
os.truncate(fd, n)  # resize file
mm = mmap.mmap(fd, n, mmap.MAP_SHARED, mmap.PROT_WRITE)  # it has to be only for writing
try:
    while True:
        ret, img = cap.read()
        if not ret:
            break            
        # write image
        buf = img.tobytes()
        start = time.perf_counter()
        mm.seek(0)
        mm.write(buf)
        mm.flush()
        stop = time.perf_counter()        
        print("Writing Duration:", (stop - start) * 1000, "ms")
except KeyboardInterrupt:
    pass
print("Closing resources")
cap.release()
mm.close()

# write max: 18ms