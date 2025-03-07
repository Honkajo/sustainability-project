import random

def efficient_pair_generation(list1, list2):
    # Use list comprehension to generate all pairs
    result = [(x, y) for x in list1 for y in list2]
    return result

# Example usage
random.seed(0)
L_size = 6000  # int to pass to range
L = [random.random() for _ in range(L_size)]
L2 = [random.random() for _ in range(L_size)]

result = efficient_pair_generation(L, L2)

