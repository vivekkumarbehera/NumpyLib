import numpy as np
array1=np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9],
                   [10, 11, 12]])
#array1[start:stop:step]
print(array1[0:3:2]) # Slicing rows 1 to 2 and columns 0 to 2 with a step of 2
print(array1[:,0:2]) 
# Slicing all rows and columns 0 to 2 with a step of 2
print(array1[0:2, 0:2]) # Slicing rows 1 to 2 and columns 0 to 2