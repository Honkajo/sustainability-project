import random

def this_func(list1, list2):
    result = []
    
    for i in range(len(list1)):
        for j in range(i, i + 1):  
            for k in range(len(list2)):
                for l in range(k, k + 1):
                    result.append((list1[i], list2[k]))
    
    return result

random.seed(0)
L_size = 6000 # int to pass to range
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
