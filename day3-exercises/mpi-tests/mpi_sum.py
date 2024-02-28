import numpy
#import mpi4py
from mpi4py import MPI

# define the number of proccesses
n_proc = 10
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# total sum of ranks
rank_sum = comm.reduce(rank, op=MPI.SUM, root=0)

print("Currently process ", rank, " is working!")

if rank == 0:
    print('The sum of the ranks is ', rank_sum)

