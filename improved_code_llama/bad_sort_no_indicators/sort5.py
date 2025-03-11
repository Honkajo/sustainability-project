import random
import numpy as np

random.seed(0)
L_size = 300000 
L = np.random.rand(L_size)

def this_func(arr):
    if len(arr) <= 1:
        return arr  

    mid = len(arr) // 2  

    left = this_func(arr[:mid])
    right = this_func(arr[mid:])

    return np.concatenate((left, right))

L = this_func(L)

