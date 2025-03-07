import random

def this_func(arr):
    return sorted(arr)  # Use Python's highly optimized Timsort

random.seed(0)
L_size = 300000
L = [random.random() for _ in range(L_size)]  # Efficiently populate the list

sorted_L = this_func(L)  # Sort the list
