"""
Continuously read images from a memory-mapped file and show them on a window.
"""
import mmap
import time
import os
import numpy as np
import matplotlib.pyplot as plt

shape = (720, 1280, 3)
n = int(np.prod(shape))

img = np.zeros(shape)
im = plt.imshow(img)
fd = os.open('/tmp/mmaptest', os.O_RDONLY)
mm = mmap.mmap(fd, n, mmap.MAP_SHARED, mmap.PROT_READ)  # it has to be only for reading

while True:
    # read image
    try:
        start = time.perf_counter()
        mm.seek(0)
        buf = mm.read(n)
        stop = time.perf_counter()
        img = np.frombuffer(buf, dtype=np.uint8).reshape(shape)
        print("Reading Duration:", (stop - start) * 1000, "ms")
        im.set_data(img)
        plt.pause(0.01)
    except Exception as e:
        print(e)
        break
plt.show()
mm.close()

# read max: 0.7ms