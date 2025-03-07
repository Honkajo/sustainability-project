import random
import heapq

def heap_sort(arr):
    heapq.heapify(arr)
    sorted_arr = []
    while arr:
        sorted_arr.append(heapq.heappop(arr))
    return sorted_arr

random.seed(0)
L_size = 10000 
L = [random.random() for _ in range(L_size)]

result = heap_sort(L)

