import random

def optimized_func(vector1, vector2):
    result = [v1 + v2 for v1, v2 in zip(vector1, vector2)]
    return result

# Example usage
random.seed(0)
L_size = 10000000  # Size for the example lists

# Generate two random lists of floating point numbers
L = [random.random() for _ in range(L_size)]
L2 = [random.random() for _ in range(L_size)]

# Example vectors
vector1 = [1, 2, 3]
vector2 = [4, 5, 6]

# Perform optimized addition
result = optimized_func(vector1, vector2)

