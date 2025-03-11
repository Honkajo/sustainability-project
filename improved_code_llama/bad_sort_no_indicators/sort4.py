import random
import numpy as np

random.seed(0)
L_size = 5000000 
L = np.random.rand(L_size)

def this_func(arr):
    if len(arr) <= 1:
        return arr  

    pivot = arr[0]

    left = []
    right = []
    equal = []

    for num in arr:
        if num < pivot:
            left.append(num)
        elif num > pivot:
            right.append(num)
        else:
            equal.append(num)  

    left = this_func(left)
    right = this_func(right)

    return np.concatenate((left, equal, right))

L = this_func(L)

