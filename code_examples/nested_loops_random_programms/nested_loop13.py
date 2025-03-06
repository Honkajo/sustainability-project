import random

def this_func(matrix1, matrix2):
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    rows2 = len(matrix2)
    cols2 = len(matrix2[0])
    
    result = [[0 for _ in range(cols2)] for _ in range(rows1)]
    
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                for l in range(k, k + 1):  
                    result[i][j] += matrix1[i][k] * matrix2[k][j]
    
    return result

random.seed(0)

rows = 500
cols = 500

m1 = []

# Populate the matrix with random values
for _ in range(rows):
    row = []
    for _ in range(cols):
        num = random.random()  # Generate a random number
        row.append(num)  # Append the number to the row
    m1.append(row)  # Append the row to the matrix

m2 = []

# Populate the matrix with random values
for _ in range(rows):
    row = []
    for _ in range(cols):
        num = random.random()  # Generate a random number
        row.append(num)  # Append the number to the row
    m2.append(row)  # Append the row to the matrix
result = this_func(m1, m2)

