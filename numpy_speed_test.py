import numpy as np
import time

# Create 1 million numbers
size = 1000000

# Python List
py_list = list(range(size))
start = time.time()
py_result = [x * 2 for x in py_list]
py_time = time.time() - start

# NumPy Array
np_array = np.arange(size)
start = time.time()
np_result = np_array * 2
np_time = time.time() - start

print("Python List Time:", py_time)
print("NumPy Array Time:", np_time)
