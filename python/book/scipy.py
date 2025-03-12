import numpy as np
from scipy.linalg import solve

# Coefficients matrix
A = np.array([[2, 3], [4, 5]])

# Constants matrix
B = np.array([8, 10])

# Solving Ax = B
solution = solve(A, B)
print("Solution (x, y):", solution)
