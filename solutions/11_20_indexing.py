import numpy as np
# exo 11:
"""
Reminder:
An identity matrix (denoted I) is a square matrix with:
1s on the main diagonal (from top-left to bottom-right)
0s everywhere else 
"""
array1 = np.eye(3)
print(array1)

# exo 12:
array2 = np.random.rand(3,3,3) # You Can use randint for integer values
print(array2)

# exo 13:
array3 = np.random.rand(10,10) 
min_array3 = array3.min()
max_array3 = array3.max()
print(f"array = {array3}")
print("min is: {} and max is: {}".format(min_array3, max_array3))

# exo 14:
array4 = np.random.rand(30)
mean = array4.mean()
print(f"array = {array4}")
print(f"mean = {mean}")

# exo 15:
array5 = np.ones((5,5))
array5[1:4, 1:4] = 0
print(array5)

# exo 16:
def add_border_of_0s(arr):
    return np.pad(arr, 1)

# Test: 
print(add_border_of_0s(np.array([[1,2],[3,4]])))

# exo 17:
"""
Output: 
0 * np.nan         = nan
np.nan == np.nan   = False
np.inf > np.nan    = False
np.nan - np.nan    = nan
np.nan in set([np.nan]) = True
0.3 == 3 * 0.1     = False
"""

# exo 18:
values = [1,2,3,4]
array6 = np.zeros((5,5), dtype=int)
array6[1: , :-1] = np.diag(values)
print(array6)

# exo 19:
array7 = np.zeros((8,8))
array7[::2, 1::2] = 1 # even rows, odd cols
array7[1::2, ::2] = 1 # odd rows, even cols
print(array7)

# exo 20:
index = np.unravel_index(99, (6,7,8))
print(index)