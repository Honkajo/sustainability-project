import random

random.seed(0)
L_size = 20000
L = [random.random() for _ in range(L_size)]

def find_duplicates(lst):
    seen = set()
    duplicates = set()
    
    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    
    return list(duplicates)

# Find duplicates
find_duplicates(L)

