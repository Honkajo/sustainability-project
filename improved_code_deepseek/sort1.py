import random

def efficient_find_duplicates(lst):
    seen = set()
    duplicates = set()
    
    for num in lst:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    
    return list(duplicates)

# Example usage
random.seed(0)
L_size = 20000
L = [random.random() for _ in range(L_size)]  # Efficiently populate the list

duplicates = efficient_find_duplicates(L)

