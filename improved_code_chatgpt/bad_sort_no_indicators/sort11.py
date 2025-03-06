import random

def this_func_1(a):
    return sorted(a)  # Uses Timsort (O(n log n))

random.seed(0)
k = 20_000  
l = [random.random() for _ in range(k)]  # Faster list creation

this_func_1(l)

