import random

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

random.seed(0)
L_size = 10000 
L = [random.random() for _ in range(L_size)]

result = insertion_sort(L)

