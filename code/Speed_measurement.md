# Code, um die Geschwindigkeit der KI auf dem Raspberry Pi zu messen
```
import time
import numpy as np
import cv2
from ultralytics import YOLO

# loads the modell
model = YOLO("best.pt")

# dummy test images
img = np.random.randint(0, 255, (480, 640, 3), dtype=np.uint8)

# warms up
for _ in range(2):
    model.predict(img, verbose=False)

# time measuring over several images
N = 20
times = []
for _ in range(N):
    t1 = time.perf_counter()
    model.predict(img, verbose=False)
    t2 = time.perf_counter()
    times.append(t2 - t1)

avg_time = np.mean(times)
fps = 1 / avg_time

print(f"Average inference time: {avg_time*1000:.2f} ms")
print(f"Average speed: {fps:.2f} FPS")
```
