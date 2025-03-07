import random

def this_func_1(a):
    return sorted(a)  # Use Python's highly optimized Timsort

random.seed(0)
g = 10000
h = [random.random() for _ in range(g)]  # Efficiently populate the list

sorted_h = this_func_1(h)  # Sort the list
