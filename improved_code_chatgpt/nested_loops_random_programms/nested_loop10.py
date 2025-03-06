import random

def optimized_func(list1, list2):
    result = [(list1[i], list2[k]) for i in range(len(list1)) for k in range(len(list2))]
    return result

# Example usage
random.seed(0)
L_size = 6000  # Size for the lists

# Generate two random lists
L = [random.random() for _ in range(L_size)]
L2 = [random.random() for _ in range(L_size)]

# Perform the optimized function
result = optimized_func(L, L2)

