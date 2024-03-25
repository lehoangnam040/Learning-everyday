from multiprocessing.shared_memory import SharedMemory
import time
import numpy as np

# import cv2 as cv

# shape = (720, 1280, 3)
shape = (3000, 4000, 3)
N = int(np.prod(shape))

print("Opening camera...")
# cap = cv.VideoCapture(0)
# cap.set(cv.CAP_PROP_FRAME_WIDTH, shape[1])
# cap.set(cv.CAP_PROP_FRAME_HEIGHT, shape[0])

sm = SharedMemory(name="namlh", create=True, size=N)
img = np.ndarray(shape, dtype=np.uint8, buffer=sm.buf)
img.fill(0)
try:
    while True:
        # img = np.random.rand()
        # ret, img = cap.read()
        # if not ret:
        #     break
        _val = np.random.rand(*shape).astype(np.uint8)

        # write image
        start = time.perf_counter()
        img[:,:,:] = _val
        stop = time.perf_counter()

        print("Writing Duration:", (stop - start) * 1000, "ms")
except KeyboardInterrupt:
    pass
print("Closing resources")
# cap.release()
sm.close()
sm.unlink()