import random

def this_func_optimized(rows, cols):
    # Generate two random matrices with values between 1 and 10
    matrix1 = [[random.randint(1, 10) for _ in range(cols)] for _ in range(rows)]
    matrix2 = [[random.randint(1, 10) for _ in range(cols)] for _ in range(rows)]
    
    # Add the two matrices element-wise
    result = [[matrix1[i][j] + matrix2[i][j] for j in range(cols)] for i in range(rows)]
    
    return result

# Example usage
rows, cols = 2500, 2500
result = this_func_optimized(rows, cols)

