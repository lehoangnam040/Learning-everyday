from multiprocessing.shared_memory import SharedMemory
from multiprocessing import resource_tracker
import time
import numpy as np
import matplotlib.pyplot as plt

sm = SharedMemory(name="namlh")
resource_tracker.unregister(f"/{sm.name}", "shared_memory")
# shape = (720, 1280, 3)
shape = (3000, 4000, 3)

# img = np.zeros(shape)
# im = plt.imshow(img)

while True:
    # read image
    try:
        start = time.perf_counter()
        img = np.frombuffer(sm.buf[:], dtype=np.uint8).reshape(shape)
        stop = time.perf_counter()

        print("Reading Duration:", (stop - start) * 1000, "ms", img.shape)
        # im.set_data(img)
        plt.pause(0.01)
    except:
        break
    
sm.close()
plt.show()
