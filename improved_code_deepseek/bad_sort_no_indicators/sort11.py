import random

def this_func_1(a):
    return sorted(a)  # Use Python's highly optimized Timsort

random.seed(0)
k = 20000
l = [random.random() for _ in range(k)]  # Efficiently populate the list

sorted_l = this_func_1(l)  # Sort the list
