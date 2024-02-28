import numpy
#import mpi4py
from mpi4py import MPI


# define the number of proccesses
n_proc = 10
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

print("Currently process ", rank, " is working!")