import random

def smoothsort(arr):
    fibs = [1, 1]
    while fibs[-1] < len(arr):
        fibs.append(fibs[-1] + fibs[-2])
    heap = []
    for num in arr:
        heapq.heappush(heap, num)
    sorted_arr = []
    while heap:
        sorted_arr.append(heapq.heappop(heap))
    return sorted_arr

random.seed(0)
L_size = 20000 
L = [random.random() for _ in range(L_size)]

result = smoothsort(L)

