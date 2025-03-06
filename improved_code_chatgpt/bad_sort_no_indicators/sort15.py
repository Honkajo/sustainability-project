import random

def this_func_3(a):
    return sorted(a)  # Uses Timsort (O(n log n))

random.seed(0)
f = 10
g = [random.random() for _ in range(f)]  # Efficient list initialization

this_func_3(g)

