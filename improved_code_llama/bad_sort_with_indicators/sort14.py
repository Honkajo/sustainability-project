import random

def swapsort(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

random.seed(0)
L_size = 30000 
L = [random.random() for _ in range(L_size)]

result = swapsort(L)

