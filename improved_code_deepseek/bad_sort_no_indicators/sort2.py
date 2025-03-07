import random

random.seed(0)
L_size = 10000
L = [random.random() for _ in range(L_size)]  # Efficient list creation

def this_func(arr):
    return sorted(arr)  # Use Python's highly optimized Timsort

sorted_L = this_func(L)
