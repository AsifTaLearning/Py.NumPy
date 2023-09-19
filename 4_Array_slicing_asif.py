import numpy as np

# NumPy Array Slicing
# Slicing arrays

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5])

# Another example

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[4:])

# Another example

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[:4])

# Negative Slicing

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[-3:-1])

# STEP

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5:2])

# Another example

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[::2])

# Slicing 2-D Arrays

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[1, 1:4])

# Another example

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[0:2, 2])

# Another example

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[0:2, 1:4])



