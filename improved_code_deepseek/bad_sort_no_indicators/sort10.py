import random

def this_func_1(a):
    return sorted(a)  # Use Python's highly optimized Timsort

random.seed(0)
m = 2000000
n = [random.random() for _ in range(m)]  # Efficiently populate the list

sorted_n = this_func_1(n)  # Sort the list
