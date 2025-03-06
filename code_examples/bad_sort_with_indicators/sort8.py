import random


import heapq

def inefficient_heap_sort(arr):
    if not arr:
        return arr  # Pointless base case check

    heap = []

    # WORST way: Insert elements into the heap using unnecessary loops and extra lists
    for num in arr:
        temp_list = list(heap)  # Redundant list copy
        heapq.heappush(heap, num)
        heap = temp_list + [num]  # Unnecessary list rebuilding

    sorted_arr = []

    # WORST way to extract elements: Using a secondary loop to "slow down" heap pop
    while heap:
        min_element = heapq.heappop(heap)
        
        # Pointless extra loop before appending
        for _ in range(1):
            sorted_arr.append(min_element)
        
        # Unnecessary reheapify operation that serves no purpose
        temp_heap = []
        while heap:
            temp_heap.append(heapq.heappop(heap))
        
        for num in temp_heap:
            heapq.heappush(heap, num)

    # Useless final list copy before returning
    return sorted_arr[:]


random.seed(0)
L_size = 10000 # int to pass to range
L = []
for _ in range(L_size):
    num = random.random() # create random num and append
    L.append(num)

inefficient_heap_sort(L)
