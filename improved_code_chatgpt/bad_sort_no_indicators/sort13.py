import random

def this_func_1(a):
    return sorted(a)  # Uses Timsort (O(n log n))

random.seed(0)
n = 20_000
o = [random.random() for _ in range(n)]  # Efficient list initialization

this_func_1(o)

