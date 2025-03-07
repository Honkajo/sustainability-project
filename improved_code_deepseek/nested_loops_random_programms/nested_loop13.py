import numpy as np

def efficient_matrix_multiplication(matrix1, matrix2):
    # Convert lists to NumPy arrays
    matrix1 = np.array(matrix1)
    matrix2 = np.array(matrix2)
    
    # Perform matrix multiplication using NumPy
    result = np.dot(matrix1, matrix2)
    
    return result

# Example usage
random.seed(0)

rows = 500
cols = 500

# Populate the matrices with random values using NumPy
m1 = np.random.rand(rows, cols)
m2 = np.random.rand(rows, cols)

result = efficient_matrix_multiplication(m1, m2)
