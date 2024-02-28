# Program to multiply two matrices using nested loops

### THE BEST PERFORMANCE I GOT WAS 0.1755941 sec total

import random
import cProfile
import numpy as np

N = 250

# NxN matrix
@profile
def get_matrix_X():
    X = np.random.randint(100, size=(N, N))
   
    return X

# Nx(N+1) matrix
@profile
def get_matrix_Y():
    
    Y = np.random.randint(100, size=(N, N+1))
   
    return Y

# result is Nx(N+1)

@profile
def get_product():  

    X = get_matrix_X()
    Y = get_matrix_Y()

    # we can simply use numpy instead of nested loops which saves a lot of time
    result = np.dot(X, Y)
    
    return result

@profile
def print_matrix_elemets(result):
    for r in result:
        print(r)
  
result = get_product()

print_matrix_elemets(result)

