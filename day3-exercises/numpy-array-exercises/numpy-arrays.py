import numpy as np


# a. Create a null vector of size 10 but the fifth value which is 1
my_vec = np.zeros(10)
my_vec[4] = 1

# b. Create a vector with values ranging from 10 to 49
my_vec =  np.random.randint(10, 49, 10)

# c. Reverse a vector (first element becomes last)
my_vec[::-1]

# d. Create a 3x3 matrix with values ranging from 0 to 8
my_matr = np.random.randint(8, size=(3, 3))

# e. Find indices of non-zero elements from [1,2,0,0,4,0]
#my_matr[[1,2,0,0,4,0]] != 0 
## ??

# f. Create a random vector of size 30 and find the mean value
vec_mean = np.random.rand(30).mean()

# g. Create a 2d array with 1 on the border and 0 inside
matr = np.matrix('1 1 1; 1 0 1; 1 1 1')

# h. Create a 8x8 matrix and fill it with a checkerboard pattern

#first_row = np.concatenate([[0, 1]] * 4, axis = 0)
chess_matr = np.indices([8, 8]).sum(axis=0) % 2
# np.indicies creates 2 arrays, first with rows in ascending order, second is transposed first.
# if we sum them element-wise as matrices, we get another matrix, where eevry second element is even
# thus taking the %2 we get 0 and 1

# i. Create a checkerboard 8x8 matrix using the tile function
chess_matr = np.tile( np.array([[0,1],[1,0]]), (4, 4))

# j. Given a 1D array, negate all elements which are between 3 and 8, in place
my_vec =  np.random.randint(1, 10, 10)
-abs(my_vec[(my_vec <= 8) * (my_vec >= 3)])

# Create a random vector of size 10 and sort it
my_vec.sort()

#  Consider two random array A anb B, check if they are equal
A =  np.random.randint(1, 10, 10)
B =  np.random.randint(1, 10, 10)
# compare A and B an
print((A == B).all())

# m. How to calculate the square of every number in an array in place (without creating temporaries)?
Z = np.arange(10, dtype=np.int32)
Z_squared = np.power(Z, 2)

#  How to get the diagonal of a dot product?
A = np.arange(9).reshape(3,3)
B = A + 1
C = np.dot(A,B)
C_diag = C.diagonal()

