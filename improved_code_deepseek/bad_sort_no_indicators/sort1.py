import random

random.seed(0)
L_size = 20000 
L = [random.random() for _ in range(L_size)]  # More efficient list creation

def this_func(lst):
    seen = {}
    duplicates = set()
    
    for num in lst:
        if num in seen:
            duplicates.add(num)
        else:
            seen[num] = 1
    
    return list(duplicates)

duplicates = this_func(L)
print(duplicates)
