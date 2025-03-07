import random
import numpy as np

def this_func(vector1, vector2):
    return np.array(vector1) * np.array(vector2)

random.seed(0)
L_size = 20000000 
L = [random.random() for _ in range(L_size)]
L2 = [random.random() for _ in range(L_size)]

result = this_func(L, L2)

