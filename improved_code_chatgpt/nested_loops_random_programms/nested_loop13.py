import random

def optimized_func(matrix1, matrix2):
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    rows2 = len(matrix2)
    cols2 = len(matrix2[0])
    
    # Initialize the result matrix with zeros
    result = [[0 for _ in range(cols2)] for _ in range(rows1)]
    
    # Perform matrix multiplication (without the redundant loops)
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    
    return result

random.seed(0)

rows = 500
cols = 500

# Generate matrix m1 with random values
m1 = [[random.random() for _ in range(cols)] for _ in range(rows)]

# Generate matrix m2 with random values
m2 = [[random.random() for _ in range(cols)] for _ in range(rows)]

# Perform the optimized matrix multiplication
result = optimized_func(m1, m2)

