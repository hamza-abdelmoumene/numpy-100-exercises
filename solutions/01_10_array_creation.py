# exo 01:
import numpy as np

# exo 02:
# Print the NumPy version:
print("NumPy Version: ", np.__version__)

# Print build configuration:
print("NumPy Configuration:")
np.show_config()

# exo 03:
array1 = np.zeros((10,)) # null vector of size 10 (float type)
print(array1)

# exo 04:
def memory_size(arr):
    return arr.nbytes
# Test: 
print(memory_size(array1)) # 80 bytes

# exo 05:
help(np.add) 

# exo 06:
array2 = np.zeros((10,))
array2[4] = 1 
print(array2)

# exo 07:
array3 = np.arange(10, 50)
print(array3)

# exo 08:
def reverse_vecotor(arr):
    return arr[::-1] # slicing ^^
# Test:
print(reverse_vecotor(array3))

# exo 09:
array4 = np.arange(0, 9).reshape((3, 3))
print(array4)

# exo 10:
arr = np.array([1,2,0,0,4,0])
indices = np.nonzero(arr)
print(indices) # [0,1,4]
