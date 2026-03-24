import numpy as np 
# exo 31:
np.seterr(all='ignore')
array1 = np.array([1,2,3]) 
print(array1 / 0) # result = [inf inf inf] (dividing by zero !)

# exo 32:
'''
the expression: "np.sqrt(-1) == np.emath.sqrt(-1)" is not true because one returns nan, the other returns a complex number (i = sqrt(-1))
'''

# exo 33:
today = np.datetime64('today')
tomorrow = np.timedelta64(1, 'D') + today
yesterday = today - np.timedelta64(1, 'D') 
print(f"today is: {today}\nyesterday is: {yesterday}\ntomorrow is: {tomorrow}")

# exo 34:
july_2025 = np.arange('2025-07', '2025-08', dtype='datetime64[D]')
print(july_2025)

# exo 35: 
# calculating (A+B)*(-A/2) directly: 
A = np.ones(3) * 1
B = np.ones(3) * 2
result = np.multiply(np.add(A, B), np.divide(np.multiply(A, -1), 2))
print(result) # [-1.5 -1.5 -1.5]

# exo 36:
arr = np.random.uniform(0, 10, 5)
print(np.floor(arr))
print(np.ceil(arr) - 1)
print(np.trunc(arr))
print(arr.astype(int))
# bonus ^^:
updated_fix = lambda x: np.sign(x) * np.fix(np.abs(x))
print(updated_fix(arr))

# exo 37:
array2 = np.zeros((5,5)) + np.arange(5) # broadcasting ^^
print(array2)

# exo 38:
def generate():
    for x in range(10):
        yield x

array3 = np.fromiter(generate(), dtype=int)
print(array3)

# exo 39:
array4 = np.arange(1,10)/10
print(array4)

# exo 40:
not_sorted = np.random.randint(100, size = 10)
sorted_arr = np.sort(not_sorted)
print(sorted)
