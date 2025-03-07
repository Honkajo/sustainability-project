import random
import numpy as np

def this_func(rows, cols):
    matrix1 = np.random.randint(1, 10, size=(rows, cols))
    matrix2 = np.random.randint(1, 10, size=(rows, cols))
    
    return np.dot(matrix1, matrix2)

# Example usage
rows, cols = 2500, 2500
result = this_func(rows, cols)

