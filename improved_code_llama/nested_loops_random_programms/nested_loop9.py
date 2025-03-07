import random
import numpy as np

def this_func(vector1, vector2):
    return np.array(vector1) + np.array(vector2)

# Example usage
random.seed(0)
L_size = 10000000 
L = [random.random() for _ in range(L_size)]
L2 = [random.random() for _ in range(L_size)]

vector1 = [1, 2, 3]
vector2 = [4, 5, 6]

result = this_func(vector1, vector2)

