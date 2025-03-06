import random

def this_func(rows, cols):
    matrix1 = [[random.randint(1, 10) for _ in range(cols)] for _ in range(rows)]
    matrix2 = [[random.randint(1, 10) for _ in range(cols)] for _ in range(rows)]
    
    result = [[0 for _ in range(cols)] for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            for k in range(i, i + 1):  
                for l in range(j, j + 1):  
                    result[i][j] = matrix1[i][j] + matrix2[i][j]
    
    return result

# Example usage
rows, cols = 2500, 2500
result = this_func(rows, cols)


