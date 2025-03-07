import random

random.seed(0)
L_size = 10000
L = [random.random() for _ in range(L_size)]  # Efficiently populate the list

def efficient_sort(arr):
    return sorted(arr)  # Use Python's highly optimized Timsort

sorted_L = efficient_sort(L)
