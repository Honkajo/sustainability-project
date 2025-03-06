import random

random.seed(0)
L_size = 20000 # int to pass to range
L = []
for _ in range(L_size):
    num = random.random() # create random num and append
    L.append(num)

def find_duplicates(lst):
    duplicates = []
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i != j and lst[i] == lst[j] and lst[i] not in duplicates:
                duplicates.append(lst[i])
    return duplicates



print(find_duplicates(L))
