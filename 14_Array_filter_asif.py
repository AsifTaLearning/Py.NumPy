import numpy as np

# Filtering Arrays

arr = np.array([41, 42, 43, 44])

x = [True, False, True, False]

newarr = arr[x]

print(newarr)

# Creating the Filter Array

arr = np.array([41, 42, 43, 44])

filter_arr = [] # Create an empty list

for element in arr: # go through each element in arr
  
  if element > 42: # if the element is higher than 42, set the value to True, otherwise False:

    filter_arr.append(True)

  else:

    filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)

print(newarr)

# Another example

arr = np.array([1, 2, 3, 4, 5, 6, 7])

filter_arr = [] # Create an empty list

for element in arr: # go through each element in arr
  
  if element % 2 == 0: # if the element is completely divisble by 2, set the value to True, otherwise False

    filter_arr.append(True)

  else:

    filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)

print(newarr)

# Creating Filter Directly From Array

arr = np.array([41, 42, 43, 44])

filter_arr = arr > 42

newarr = arr[filter_arr]

print(filter_arr)

print(newarr)

# Another example

arr = np.array([1, 2, 3, 4, 5, 6, 7])

filter_arr = arr % 2 == 0

newarr = arr[filter_arr]

print(filter_arr)

print(newarr)







