import random
import numpy as np

def this_func(vector1, vector2):
    return [(x * y) for x in vector1 for y in vector2]

random.seed(0)
L_size = 6000 
L = [random.random() for _ in range(L_size)]
L2 = [random.random() for _ in range(L_size)]

result = this_func(L, L2)

