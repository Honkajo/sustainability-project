import random
import numpy as np

random.seed(0)
L_size = 10000 
L = np.random.rand(L_size)

def this_func(arr):
    arr.sort()
    return arr

L = this_func(L)

