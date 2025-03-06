import random
from collections import Counter

random.seed(0)
L_size = 20000
L = [random.random() for _ in range(L_size)]  # List comprehension for efficiency

def this_func(lst):
    count = Counter(lst)  # Count occurrences of each number
    return [num for num, freq in count.items() if freq > 1]  # Extract duplicates

this_func(L)
