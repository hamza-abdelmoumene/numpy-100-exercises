import random

import numpy as np


np.random.seed(42)
random.seed(42)


def title(exo: int, text: str) -> None:
    print(f"\nEXO {exo:02d} - {text}")
    print("-" * 44)


# exo 41
title(41, "Array Sum With Reduce")
array1 = [1, 2, 3, 4]
print(f"Input: {array1}")
print(f"Sum: {np.add.reduce(array1)}")


# exo 42
title(42, "Array Equality")
A = np.random.randint(0, 2, 5)
B = np.random.randint(0, 2, 5)
print(f"A: {A}")
print(f"B: {B}")
print("Result: Equal" if np.array_equal(A, B) else "Result: Not equal")


# exo 43
title(43, "Read-Only Array")
array2 = np.array([1, 2, 3, 4, 5])
array2.setflags(write=False)
print(f"Before write attempt: {array2}")
try:
    array2[2] = 99
except ValueError:
    print("Write blocked: cannot modify read-only array")


# exo 44
title(44, "Cartesian To Polar")
cartesian = np.random.uniform(-10, 10, (3, 2))
x, y = cartesian[:, 0], cartesian[:, 1]
r = np.sqrt(x**2 + y**2)
theta = np.arctan2(y, x)
polar = np.column_stack([r, theta])
print("Cartesian (x, y):")
print(np.round(cartesian, 3))
print("Polar (r, theta):")
print(np.round(polar, 3))


# exo 45
title(45, "Replace Maximum Value")
array3 = np.random.uniform(-10, 10, 10)
max_index = array3.argmax()
max_value = array3[max_index]
array3[max_index] = 0
print(f"Max value {max_value:.3f} at index {max_index} replaced by 0")
print(f"Updated array: {np.round(array3, 3)}")


# exo 46
title(46, "Structured 2D Grid")
dtype = [("x", "f8"), ("y", "f8")]
n = 5
x_vals = np.linspace(0, 1, n)
y_vals = np.linspace(0, 1, n)
X, Y = np.meshgrid(x_vals, y_vals)

# Build a 1D structured array where each element is a point (x, y).
grid = np.zeros(X.size, dtype=dtype)
grid["x"] = X.ravel()
grid["y"] = Y.ravel()

print(f"Total points: {grid.size}")
print(f"First point: {grid[0]}")
print(f"Last point:  {grid[-1]}")
print(f"x field (first 8): {grid['x'][:8]}")
print(f"y field (first 8): {grid['y'][:8]}")


# exo 47
title(47, "Cauchy Matrix")
X = np.arange(8)
Y = X + random.random()
cauchy = 1.0 / (X.reshape(-1, 1) - Y.reshape(1, -1))
print(f"X: {X}")
print(f"Y: {np.round(Y, 3)}")
print("Cauchy matrix:")
print(np.round(cauchy, 3))


# exo 48
title(48, "NumPy Type Limits")
type_names = [
    "int8",
    "int16",
    "int32",
    "int64",
    "uint8",
    "uint16",
    "uint32",
    "uint64",
    "float16",
    "float32",
    "float64",
    "float128",
]

print(f"{'Type':12} | {'Min':>20} | {'Max':>20}")
print("-" * 60)
print(f"{'bool':12} | {'False':>20} | {'True':>20}")

for name in type_names:
    try:
        dtype = np.dtype(name)
    except TypeError:
        print(f"{name:12} | {'N/A':>20} | {'N/A':>20}")
        continue

    if np.issubdtype(dtype, np.integer):
        info = np.iinfo(dtype)
        min_str = str(info.min)
        max_str = str(info.max)
    else:
        info = np.finfo(dtype)
        min_str = np.format_float_scientific(info.min, precision=4, unique=False)
        max_str = np.format_float_scientific(info.max, precision=4, unique=False)

    print(f"{name:12} | {min_str:>20} | {max_str:>20}")


# exo 49
title(49, "Large Array Display")
array4 = np.arange(1000)
print(f"Shape: {array4.shape}, dtype: {array4.dtype}")
print(f"First 10: {array4[:10]}")
print(f"Last 10:  {array4[-10:]}")


# exo 50
title(50, "Nearest Value Index")
array5 = np.arange(100)
value = 42.7
target = np.abs(array5 - value).argmin()
print(f"Target value: {value}")
print(f"Nearest index: {target}")
print(f"Nearest value: {array5[target]}")
