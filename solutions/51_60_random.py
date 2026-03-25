import numpy as np
from pathlib import Path

def title(exo: int, text: str) -> None:
    print(f"\nEXO {exo:02d} - {text}")
    print("-" * 44)

# exo 51:
title(51, "Create a structured array representing a position and a color")
type1 = np.dtype([('position', [('x',float),('y',float)]), ('color', [('r',float),('g',float),('b',float)])])
print(type1)

# exo 52:
title(52, "Negate [0.2, 0.8] interval")
array1 = np.random.rand(10)
array1[(array1 > 0.2) & (array1 < 0.8)] *= -1
print(array1)

# exo 53: 
title(53, "Float array to Int one in place (No Copying)")
array2 = np.arange(10, dtype=np.float64)
print(f"floats: {array2}")
array2 = array2.astype(int, copy=False)
print(f"integers: {array2}")

# exo 54:
csv_path = Path(__file__).resolve().parent / "file.csv"
title(54, "Generate from file")
array3 = np.genfromtxt(csv_path, delimiter=",")
print(array3)
# exo 55:
title(55, "Enumerate Numpy Arrays")
enum_arr = np.array([10, 20, 30])
for index, value in np.ndenumerate(enum_arr):
    print(f"(index: {index}, value: {value})")


# exo 56:
title(56, "Generate Gaussian-Like Array (10, 10): ")
# Step 1: Create coordinate grid
size = 10
x = np.linspace(-3, 3, size)
y = np.linspace(-3, 3, size)
X, Y = np.meshgrid(x, y)

# Step 2: Gaussian formula = exp(-distance^2)
gaussian = np.exp(- (X**2 + Y**2) / 2)

print("10x10 Gaussian array:")
print(np.round(gaussian, 2))

# exo 57:
title(57, "Randomly place p elements in a 2D array")
n = 10
p = 3

array4 = np.zeros((n, n), dtype=int)

indices = np.random.choice(n*n, size=p, replace=False)

np.put(array4, indices, 1)
print(array4) # everytime the output change

# exo 58:
title(58, "Subtract the mean of each row of a matrix: ")
array5 = np.array([[1,2,3], [10,20,30], [100, 200, 300]])
array5 = array5 - array5.mean(axis=1, keepdims=True)
print(array5)

# exo 59:
title(59, "Sort an array by the nth column")
array6 = np.array([[3,1],
                [2,4],
                [1,3]])
# sort by column 1
# Expected: [[3,1],[1,3],[2,4]]
sorted_array6 = array6[array6[:, 1].argsort()]
print(sorted_array6)

# exo 60:
title(60, "Tell if a given 2D array has null columns")
arr = np.array([[1, 0, 3],
                [4, 0, 6],
                [7, 0, 9]])
has_null_column = (~arr.any(axis=0)).any()
print(f"Does it have a null column? {has_null_column}")