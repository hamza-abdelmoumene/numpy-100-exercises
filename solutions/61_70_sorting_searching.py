import numpy as np
# exo 61:
array1 = np.random.uniform(0, 1, 10)
target = 0.5
# Expected: closest value in arr to 0.5
value = array1.flat[np.abs(array1 - target).argmin()]
print(f"target = {target}\narray = {array1} \nclosest value = {value}")

# exo 62:
A = np.arange(3).reshape(1, 3)
B = np.arange(3).reshape(3, 1)
print(f"{A + B}")

# exo 63:
array2 = np.random.rand(10)
result = array2[(array2 >= 0.1) & (array2 <= 0.9)]
print(result)

# exo 64:
array3 = np.random.uniform(0, 1, (10, 2))
point = np.array([0.5, 0.5])
print(array3)
print(np.argmin(np.linalg.norm(array3 - point, axis=1)))

# exo 65:
array4 = np.array([1, 2, 3, 4, 5])
acum_sum = np.cumsum(array4)
print(acum_sum) # Expected: [1, 3, 6, 10, 15]

# exo 66: 
array5 = np.arange(10)
array5 = array5[np.arange(8)[:, None] + np.arange(3)]
print(array5)

# exo 67:
arr_bool = np.array([True, False, True])
arr_float = np.array([1.0, -2.0, 3.0])
np.logical_not(arr_bool, out=arr_bool) 
np.negative(arr_float, out=arr_float)
print(f"{arr_bool}\n{arr_float}")

# exo 68: 
P0 = np.random.uniform(-2, 2, (3, 2))
P1 = np.random.uniform(-2, 2, (3, 2))
p = np.array([0.0, 0.0])

distances = np.abs(np.cross(P1 - P0, P0 - p)) / np.linalg.norm(P1 - P0, axis=1)

print("P0:\n", P0)
print("P1:\n", P1)
print("p:", p)
print("Distances:", distances)

# exo 69:
A = np.random.randint(0, 10, (8, 3))
B = np.random.randint(0, 10, (2, 2))

print("A (8x3):\n", A)
print("B (2x2):\n", B)

matches = np.where((A[:, None] == B).all(axis=2).any(axis=1))[0]
print("Matching row indices:", matches)

# exo 70:
def extract_subarray(arr, center_idx, shape):
    rows, cols = arr.shape
    r, c = center_idx
    target_rows, target_cols = shape

    row_slice = slice(max(r - target_rows//2, 0), 
                      min(r + (target_rows//2) + 1, rows))
    col_slice = slice(max(c - target_cols//2, 0), 
                      min(c + (target_cols//2) + 1, cols))
    
    sub = arr[row_slice, col_slice]
    
    pad_row = (target_rows//2 - row_slice.stop + row_slice.start, 
               target_rows//2 - (rows - row_slice.stop))
    pad_col = (target_cols//2 - col_slice.stop + col_slice.start, 
               target_cols//2 - (cols - col_slice.stop))
    
    return np.pad(sub, ((pad_row[0], pad_row[1]), (pad_col[0], pad_col[1])), 
                  mode='constant')

# Test
np.random.seed(42)
arr = np.random.randint(0, 10, (8, 8))
center = (2, 3)
subarray = extract_subarray(arr, center, (5, 5))

print("Original:\n", arr)
print("Center:", center)
print("5x5 Extracted:\n", subarray)
