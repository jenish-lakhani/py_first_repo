import numpy as np

arr = np.array([1, 2, 3])
# print(arr)

l = [1, 2, 3]
# print(l)

python_list = list(range(100))
# print(python_list[:5])

import sys

#  take less bite a numpy compare tu python
# print(sys.getsizeof(python_list[0]) * len(python_list))

numpy_array = np.arange(100)
# print(numpy_array[:5])

# print(numpy_array.nbytes) # size mate nu 6 nbytes


import time

# take less time  numpy take less time
size = 1000000
l1 = list(range(size))
l2 = list(range(size))

start_time = time.time()
l3 = [x + y for x, y in zip(l1, l2)]
end_time = time.time()

# print("python list took :", end_time - start_time)


n1 = np.arange(size)
n2 = np.arange(size)
# print(n1[:4], n2[:4])

start_time = time.time()
n3 = n1 + n2
end_time = time.time()
# print("numpyarray took :", end_time - start_time)


# convenient use with built inn function

l1 = list(range(5))
l2 = list(range(5))

l3 = [x + y for x, y in zip(l1, l2)]
print(l3)


n1 = np.arange(5)
n2 = np.arange(5)
print(list[(n1 + n2)])
