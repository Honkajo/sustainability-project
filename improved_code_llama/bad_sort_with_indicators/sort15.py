import random

def bogosort(arr):
    for _ in range(1000):  # Wahrscheinlichkeit, dass die Liste innerhalb von 1000 Schritten sortiert wird
        random.shuffle(arr)
        if is_sorted(arr):
            break
    return arr

def is_sorted(arr):
    for i in range(1, len(arr)):
        if arr[i - 1] > arr[i]:
            return False
    return True

random.seed(0)
L_size = 10 
L = [random.random() for _ in range(L_size)]

result = bogosort(L)

