import random

def this_func_1(a):
    return sorted(a)  # Uses Timsort (O(n log n))

random.seed(0)
m = 2_000_000  
n = [random.random() for _ in range(m)]  # Faster list creation

this_func_1(n)

