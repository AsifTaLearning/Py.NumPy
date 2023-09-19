import numpy as np

# Searching Arrays

arr = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr == 4)

print(x)

# Another example

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

x = np.where(arr%2 == 0)

print(x)

# Another example

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

x = np.where(arr%2 == 1)

print(x)

# Search Sorted

arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7)

print(x)

# Search From the Right Side

arr = np.array([6, 7, 8, 9 ])

x = np.searchsorted(arr, 7, side='right')

print(x)

# Multiple Values

arr = np.array([1, 3, 5, 7])

x = np.searchsorted(arr, [2, 4, 6])

print(x)




