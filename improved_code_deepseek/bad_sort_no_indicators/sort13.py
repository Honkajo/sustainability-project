import random

def this_func_1(a):
    return sorted(a)  # Use Python's highly optimized Timsort

random.seed(0)
n = 20000
o = [random.random() for _ in range(n)]  # Efficiently populate the list

sorted_o = this_func_1(o)  # Sort the list
