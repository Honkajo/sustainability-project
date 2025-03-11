import random

def this_func_2(a):
    return sorted(a)  # Use Python's highly optimized Timsort

random.seed(0)
h = 30000
i = [random.random() for _ in range(h)]  # Efficiently populate the list

sorted_i = this_func_2(i)  # Sort the list
