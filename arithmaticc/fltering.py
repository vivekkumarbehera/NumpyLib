import numpy as np

a = np.array([
    [12, 21, 3, 4, 11, 23, 22],
    [10, 15, 13, 14, 19, 17, 18],
    [25, 27, 29, 28, 26, 30, 24]
])

# Replace elements greater than 15 with their square, others remain unchanged
b = np.where(a > 15, a**2, a)
print(b)