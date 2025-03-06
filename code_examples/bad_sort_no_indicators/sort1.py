import random

random.seed(0)
L_size = 20000 
L = []
for _ in range(L_size):
    num = random.random() 
    L.append(num)

def this_func(lst):
    duplicates = []
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i != j and lst[i] == lst[j] and lst[i] not in duplicates:
                duplicates.append(lst[i])
    return duplicates



print(this_func(L))
