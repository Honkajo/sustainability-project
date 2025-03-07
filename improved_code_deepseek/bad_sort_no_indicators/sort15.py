import random

def this_func_3(a):
    return sorted(a)  # Use Python's highly optimized Timsort

random.seed(0)
f = 10
g = [random.random() for _ in range(f)]  # Efficiently populate the list

sorted_g = this_func_3(g)  # Sort the list
