import random

def this_func_3(l):
    return sorted(l)  # Use Python's highly optimized Timsort

random.seed(0)
q = 600000
r = [random.random() for _ in range(q)]  # Efficiently populate the list

sorted_r = this_func_3(r)  # Sort the list
