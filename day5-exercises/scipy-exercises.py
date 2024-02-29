from scipy import linalg
import numpy as np


# Define a matrix A

A = np.array([1, -2, 3, 4, 5, 6, 7, 1, 9]).reshape(3, 3)

#  Define a vector b
b = np.array([1, 2, 3])

# Solve the linear system of equations A x = b and check if correct

x = linalg.solve(A, b)
print('The solution of A*x = b is ', x)
# check if correct (i added round bc otherwise i get some False values, I though it was an approximation issue)
print('Are the obtained values correct?')
print(np.dot(A, x).round() == b)

# Repeat using a random 3x3 matrix B (instead of the vector b)
B = np.random.rand(3, 3)
X = linalg.solve(A, B)
print('The solution of A*X = B is ', X)
# check the matrix product
print('Are the obtained values correct?')
print(np.dot(A, X).round(5) == B.round(5))

#  Solve the eigenvalue problem for the matrix A and print the eigenvalues and eigenvectors
# get the eigenvalues (eig_vals) and eigenvectors (eig_vecs)
eig_vals, eig_vecs = linalg.eig(A)

print('eigen values: ', eig_vals)
print('eigen vectors: ', eig_vecs)
# check the second 
u = eig_vecs[:, 1]
lam = eig_vals[1]
# check if equal
print('Did we get right eigenvalues and eigenvectors?')
print(np.dot(A, u) == np.dot(lam, u))

# inverse and det

A_inv = linalg.inv(A)
A_det = linalg.det(A)
print("Inverse matrix: ", A_inv)
print("Matrix determinant: ", A_det)
# norm
A_norm = linalg.norm(A, ord = None)
# since A is 3-dimensional, we can only compute norm of 1st and 2nd order
A_norm1 = linalg.norm(A, ord = 1)
A_norm2 = linalg.norm(A, ord = 2)

print('Norm: ', A_norm)
print('Norm 1st order: ', A_norm1)
print('Norm: 2nd order', A_norm2)
