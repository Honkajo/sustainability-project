import random

def this_func_1(a):
    return sorted(a)  # Uses Python's Timsort (O(n log n))

random.seed(0)
o = 10_000  
p = [random.random() for _ in range(o)]  # Faster list creation

this_func_1(p)

