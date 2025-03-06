import random

def this_func(arr):
    return sorted(arr)  # Uses Timsort (O(n log n))

random.seed(0)
L_size = 10000
L = [random.random() for _ in range(L_size)]  # Efficient list creation

this_func(L)
