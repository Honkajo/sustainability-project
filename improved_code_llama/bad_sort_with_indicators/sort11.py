import random

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

random.seed(0)
L_size = 20000 
L = [random.random() for _ in range(L_size)]

result = selection_sort(L)

