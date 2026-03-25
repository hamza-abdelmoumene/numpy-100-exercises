import numpy as np

def title(exo: int, text: str) -> None:
    print(f"\nEXO {exo:02d} - {text}")
    print("-" * 44)

# exo 01:
title(1, "Import NumPy")

# exo 02:
title(2, "Print NumPy version and configuration")
print("NumPy Version: ", np.__version__)
print("NumPy Configuration:")
np.show_config()

# exo 03:
title(3, "Create a null vector of size 10")
array1 = np.zeros((10,))
print(array1)

# exo 04:
title(4, "Find memory size of any array")
def memory_size(arr):
    return arr.nbytes
print(memory_size(array1))

# exo 05:
title(5, "How to find documentation of NumPy add function")
help(np.add)

# exo 06:
title(6, "Create a null vector of size 10 but the fifth value is 1")
array2 = np.zeros((10,))
array2[4] = 1
print(array2)

# exo 07:
title(7, "Create a vector with values ranging from 10 to 49")
array3 = np.arange(10, 50)
print(array3)

# exo 08:
title(8, "Reverse a vector")
def reverse_vecotor(arr):
    return arr[::-1]
print(reverse_vecotor(array3))

# exo 09:
title(9, "Create a 3x3 matrix with values ranging from 0 to 8")
array4 = np.arange(0, 9).reshape((3, 3))
print(array4)

# exo 10:
title(10, "Find indices of non-zero elements")
arr = np.array([1, 2, 0, 0, 4, 0])
indices = np.nonzero(arr)
print(indices)