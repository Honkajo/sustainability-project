import random
import numpy as np

def this_func(matrix1, matrix2):
    return np.dot(matrix1, matrix2)

random.seed(0)

rows = 500
cols = 500

m1 = np.random.rand(rows, cols)
m2 = np.random.rand(rows, cols)

result = this_func(m1, m2)

