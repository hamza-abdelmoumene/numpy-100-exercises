# The following exercises uses LALG faundamentals:
import numpy as np
import random 
# exo 41:
array1  = [1,2,3,4]
print(np.add.reduce(array1)) # 10 & faster than sum

# exo 42:
A = np.random.randint(0, 2, 5)
B = np.random.randint(0, 2, 5)
print("Equal" if np.array_equal(A,B) else "Not equal")

# exo 43:
array2 = np.array([1,2,3,4,5])
array2.setflags(write= False)
try:
    array2[2] = 3
except ValueError:
    print("Cannot modify read-only array")

# exo 44:
np.random.seed(42)
cartesian = np.random.uniform(-10, 10, (3, 2))
print("Cartesian (x,y):\n", np.round(cartesian, 3))

x, y = cartesian[:, 0], cartesian[:, 1]
r = np.sqrt(x**2 + y**2)
theta = np.arctan2(y, x)

polar = np.column_stack([r, theta])
print("\nPolar (r,θ):\n", np.round(polar, 3))

# exo 45:
array3 = np.random.uniform(-10, 10, 10)
array3[array3.argmax()] = 0

# exo 46:
dtype = [('x', 'f8'), ('y', 'f8')] # f8 is float64 ^^
n = 5  
x_vals = np.linspace(0, 1, 5) 
y_vals = np.linspace(0, 1, 5) 
X, Y = np.meshgrid(x_vals, y_vals) 
points = np.column_stack([X.ravel(), Y.ravel()])  
grid = np.array(points, dtype=dtype)
print(grid[0])     # (x=0.0, y=0.0)
print(grid['x'])   # x: [0.0, 0.25, 0.5, ...]
print(grid['y'])   # y: [0.0, 0.0, 0.0, ...]

# exo 47:
X = np.arange(8)
Y = X + random.random()
CAUCHY = 1.0 / (X.reshape(-1,1) - Y.reshape(1,-1))
print(CAUCHY)

# exo 48:
type_names = [
    'int8', 'int16', 'int32', 'int64',
    'uint8', 'uint16', 'uint32', 'uint64',
    'float16', 'float32', 'float64', 'float128'
]
# Handle bool separately
print("Type           | Min             | Max\n", "-"*45)
print(f"{'bool':12} | {'False':>14} | {'True':>14}")

for name in type_names:
    dtype = np.dtype(name)
    
    if 'int' in name or 'uint' in name:
        info = np.iinfo(dtype)
        min_val, max_val = info.min, info.max
    else:
        info = np.finfo(dtype)
        min_val, max_val = info.min, info.max
    
    print(f"{name:12} | {min_val:>14} | {max_val:>14}")

# exo 49: 
np.set_printoptions(threshold=np.inf)
array4 = np.arange(1000)
print(array4)

# exo 50:
array5 = np.arange(100)
value = 42.7
target = np.abs(array5-value).argmin()
print(target)







