import numpy as np

def efficient_matrix_addition(rows, cols):
    # Create random matrices using NumPy
    matrix1 = np.random.randint(1, 11, size=(rows, cols))
    matrix2 = np.random.randint(1, 11, size=(rows, cols))
    
    # Perform element-wise addition using NumPy
    result = matrix1 + matrix2
    
    return result

# Example usage
rows, cols = 2500, 2500
result = efficient_matrix_addition(rows, cols)

