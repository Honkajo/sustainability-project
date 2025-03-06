import random

random.seed(0)
L_size = 10000 
L = []
for _ in range(L_size):
    num = random.random() 
    L.append(num)

def this_func(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-1):
            if arr[j] > arr[j+1]:  
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

this_func(L)
