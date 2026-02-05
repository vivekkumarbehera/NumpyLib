import numpy as np
a=np.array([1, 2, 3])
b=np.array([4, 5, 6])
print(a+b)  # Addition
print(a-b)  # Subtraction
print(a*b)  # Multiplication
print(a/b)  # Division  
print(a**2) # Square
print(a%b)  # Modulus
print(a//2) # Floor Division
print(a<2)  # Less than
print(a>2)  # Greater than
print(a<=2) # Less than or equal to
print(a>=2) # Greater than or equal to
print(a==2) # Equal to
print(a!=2) # Not equal to
print(np.dot(a,b)) # Dot product
print(np.cross(a,b)) # Cross product
print(np.sum(a)) # Sum of elements
print(np.prod(a)) # Product of elements
print(np.mean(a)) # Mean of elements
print(np.median(a)) # Median of elements
print(np.var(a)) # Variance of elements
print(np.sqrt(a)) # Square root of elements
print(np.log(a))  # Natural logarithm of elements
print(np.exp(a))  # Exponential of elements
print(np.sin(a))  # Sine of elements
print(np.cos(a))  # Cosine of elements
print(np.tan(a))  # Tangent of elements
print(np.arcsin(a/3)) # Inverse sine of elements
print(np.std(a))  # Standard deviation of elements
print(np.round(a)) # Rounding of elements
a[a < 2] = 0 # Setting elements in b less than 2 to 0
print(a)