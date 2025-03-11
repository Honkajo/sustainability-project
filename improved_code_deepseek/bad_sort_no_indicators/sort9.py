import random

def this_func_1(a):
    return sorted(a)  # Use Python's highly optimized Timsort

random.seed(0)
o = 10000
p = [random.random() for _ in range(o)]  # Efficiently populate the list

sorted_p = this_func_1(p)  # Sort the list
