import numpy as np 

def title(exo: int, text: str) -> None:
    print(f"\nEXO {exo:02d} - {text}")
    print("-" * 44)

# exo 31:
title(31, "Set NumPy warnings and divide by zero")
np.seterr(all='ignore')
array1 = np.array([1, 2, 3]) 
print(array1 / 0)

# exo 32:
title(32, "Compare sqrt(-1) and emath.sqrt(-1)")
'''
the expression: "np.sqrt(-1) == np.emath.sqrt(-1)" is not true because one returns nan, the other returns a complex number (i = sqrt(-1))
'''

# exo 33:
title(33, "Print yesterday, today, tomorrow dates")
today = np.datetime64('today')
tomorrow = np.timedelta64(1, 'D') + today
yesterday = today - np.timedelta64(1, 'D') 
print(f"today is: {today}\nyesterday is: {yesterday}\ntomorrow is: {tomorrow}")

# exo 34:
title(34, "Get all dates of July 2025")
july_2025 = np.arange('2025-07', '2025-08', dtype='datetime64[D]')
print(july_2025)

# exo 35:
title(35, "Compute (A+B)*(-A/2) in-place style")
A = np.ones(3) * 1
B = np.ones(3) * 2
result = np.multiply(np.add(A, B), np.divide(np.multiply(A, -1), 2))
print(result)

# exo 36:
title(36, "Extract integer part in different ways")
arr = np.random.uniform(0, 10, 5)
print(np.floor(arr))
print(np.ceil(arr) - 1)
print(np.trunc(arr))
print(arr.astype(int)) # turn floats to integers
# Bonus ^^: 
updated_fix = lambda x: np.sign(x) * np.fix(np.abs(x))
print(updated_fix(arr))

# exo 37:
title(37, "Create 5x5 matrix with row values 0..4")
array2 = np.zeros((5, 5)) + np.arange(5)
print(array2)

# exo 38:
title(38, "Create array from generator")
def generate():
    for x in range(10):
        yield x
array3 = np.fromiter(generate(), dtype=int)
print(array3)

# exo 39:
title(39, "Create vector with values 0.1 to 0.9")
array4 = np.arange(1, 10) / 10
print(array4)

# exo 40:
title(40, "Sort random vector")
not_sorted = np.random.randint(100, size=10)
sorted_arr = np.sort(not_sorted)
print(sorted)