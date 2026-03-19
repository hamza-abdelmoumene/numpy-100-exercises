import numpy as np

# exo 21:
array1 = np.tile([[1,0],[0,1]], (4,4))
print(array1)

# exo 22:
def normalize_array(arr):
    return (arr - arr.min())/(arr.max() - arr.min()) 

# Test:
array2 = np.array([1,2,3,4])
print(normalize_array(array2))

# exo 23:

# RGBA: 4 uint8 fields = 4 bytes per element
rgba_dtype = np.dtype([
    ('R', np.uint8),  # Red
    ('G', np.uint8),  # Green
    ('B', np.uint8),  # Blue  
    ('A', np.uint8)   # Alpha
])

# exo 24:
array3 = np.random.rand(5, 3)
array4 = np.random.rand(3,2)
print(f"array_1 = {array3} and array_2 = {array4}")
print(f"the result of multiplication is: {np.dot(array3, array4)}")

# exo 25:
array5 = np.arange(0, 11)
array5[(array5 >= 3) & (array5 <=8)] *= -1

# exo 26:
# Before numpy import: sum() = Python built-in
# sum(range(5), -1) = 0+1+2+3+4 starting from -1 = 9

# After: from numpy import * — sum() = numpy.sum
# numpy.sum(range(5), -1) = sum along axis=-1 = 10

# exo 27:
""" 
Z**Z -> legal
2 << Z >> 2 -> legal
Z <- Z -> legal
1j*Z -> legal
Z/1/1 -> legal
Z<Z>Z -> illegal
"""

# exo 28:
""" 
np.array(0) / np.array(0) = nan with RuntimeWarning
np.array(0) // np.array(0) = array(0) = 0 with RuntimeWarning
np.array([np.nan]).astype(int).astype(float) = array([-9.22337204e+18])
"""

# exo 29: 
def integer_part(arr):
    return np.copysign(np.ceil(np.abs(arr)), arr)

# exo 30:
def find_common(arr1, arr2):
    return np.intersect1d(arr1, arr2)

# Test: 
print(find_common(np.array([1,2,3,4]), np.array([4,5,6,7])))