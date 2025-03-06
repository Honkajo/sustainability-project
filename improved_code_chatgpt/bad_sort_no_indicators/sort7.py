import random

def this_func_1(a):
    return sorted(a)  # Uses Timsort (O(n log n))

random.seed(0)
g = 10_000  
h = [random.random() for _ in range(g)]  # Faster list creation

this_func_1(h)

