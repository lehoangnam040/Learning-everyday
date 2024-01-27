"""
Continuously read images from a memory-mapped file and show them on a window.
"""
import mmap
import time

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

shape = (720, 1280, 3)
n = np.prod(shape)
mm = mmap.mmap(-1, n)
# cv.namedWindow("output", cv.WINDOW_NORMAL)        # Create window with freedom of dimensions
# cv.resizeWindow("output", 512, 512) 


while True:
    # read image
    try:
        start = time.perf_counter()
        mm.seek(0)
        buf = mm.read(n)
        img = np.frombuffer(buf, dtype=np.uint8).reshape(shape)
        stop = time.perf_counter()

        print("Reading Duration:", (stop - start) * 1000, "ms")
        # im.set_data(img)
        # plt.pause(0.05)
        # plt.show()
        # cv.imwrite(f"{stop}.png" , img)
    except:
        break
    cv.imshow("output", img)
    key = cv.waitKey(1) & 0xFF
    key = chr(key)
    if key.lower() == "q":
        break

# cv.destroyAllWindows()
mm.close()