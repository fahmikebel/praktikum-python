import numpy as np
import cupy as cp
import time
# Numpy dan CPU
s = time.time()
x_cpu = np.ones((1000, 1000, 1000))
e = time.time()
print("Waktu yang diperlukan untuk CPU :", e - s)
# CuPy dan GPU
s = time.time()
x_gpu = cp.ones((1000, 1000, 1000))
cp.cuda.Stream.null.synchronize()
e = time.time()
print("Waktu yang diperlukan untuk GPU :", e - s)
# Nilai yang akan dikalikan dengan array
n = 5
# Numpy dan CPU
s = time.time()
x_cpu *= n
e = time.time()
print("Waktu yang diperlukan untuk CPU :", e - s)
### CuPy and GPU
s = time.time()
x_gpu *= n
cp.cuda.Stream.null.synchronize()
e = time.time()
print("Waktu yang diperlukan untuk GPU :", e - s)
