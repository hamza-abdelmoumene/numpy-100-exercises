import numpy as np

def title(exo: int, text: str) -> None:
    print(f"\nEXO {exo:02d} - {text}")
    print("-" * 44)

# exo 11:
title(11, "Create a 3x3 identity matrix")
array1 = np.eye(3)
print(array1)

# exo 12:
title(12, "Create a 3x3x3 array with random values")
array2 = np.random.rand(3, 3, 3)
print(array2)

# exo 13:
title(13, "Find minimum and maximum values")
array3 = np.random.rand(10, 10)
min_array3 = array3.min()
max_array3 = array3.max()
print(f"array = {array3}")
print("min is: {} and max is: {}".format(min_array3, max_array3))

# exo 14:
title(14, "Create a random vector of size 30 and find mean")
array4 = np.random.rand(30)
mean = array4.mean()
print(f"array = {array4}")
print(f"mean = {mean}")

# exo 15:
title(15, "Create 2D array with 1 on border and 0 inside")
array5 = np.ones((5, 5))
array5[1:4, 1:4] = 0
print(array5)

# exo 16:
title(16, "Add a border of zeros around an array")
def add_border_of_0s(arr):
    return np.pad(arr, 1)
print(add_border_of_0s(np.array([[1, 2], [3, 4]])))

# exo 17:
title(17, "Explain NumPy NaN and Inf behavior")
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
title(18, "Create a matrix with values on diagonal below main")
values = [1, 2, 3, 4]
array6 = np.zeros((5, 5), dtype=int)
array6[1:, :-1] = np.diag(values)
print(array6)

# exo 19:
title(19, "Create an 8x8 checkerboard matrix")
array7 = np.zeros((8, 8))
array7[::2, 1::2] = 1
array7[1::2, ::2] = 1
print(array7)

# exo 20:
title(20, "Unravel index 99 into shape (6,7,8)")
index = np.unravel_index(99, (6, 7, 8))
print(index)