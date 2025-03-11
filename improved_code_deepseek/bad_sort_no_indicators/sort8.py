import random

def this_func_1(j):
    return sorted(j)  # Use Python's highly optimized Timsort

random.seed(0)
r = 10000
s = [random.random() for _ in range(r)]  # Efficiently populate the list

sorted_s = this_func_1(s)  # Sort the list
