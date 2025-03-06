import random

def this_func(vector1, vector2):
    result = []
    
    for i in range(len(vector1)):
        for j in range(i, i + 1):  
            for k in range(i, i + 1):  
                result.append(vector1[i] * vector2[i])
    
    return result

random.seed(0)
L_size = 20000000 # int to pass to range
L = []
for _ in range(L_size):
    num = random.random() # create random num and append
    L.append(num)

random.seed(0)
L2 = []
for _ in range(L_size):
    num = random.random() # create random num and append
    L2.append(num)

result = this_func(L, L2)

