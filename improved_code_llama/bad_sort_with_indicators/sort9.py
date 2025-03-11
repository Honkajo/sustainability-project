import random
import heapq

def introduction_sort(arr):
    if len(arr) <= 16:
        return insertion_sort(arr)
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    middle = [x for x in arr[1:] if x == pivot]
    right = [x for x in arr[1:] if x > pivot]
    return introduction_sort(left) + middle + introduction_sort(right)

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

result = introduction_sort(L)

