import random

def this_func_2(a):
    return sorted(a)  # Uses Timsort (O(n log n))

random.seed(0)
h = 30_000
i = [random.random() for _ in range(h)]  # More efficient list creation

this_func_2(i)

