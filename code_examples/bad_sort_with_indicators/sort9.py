import random

import heapq
import sys

# WORST way: Setting recursion limit way too high (even though it's not needed)
sys.setrecursionlimit(10**6)

def inefficient_intro_sort(arr):
    max_depth = len(arr) * 2  # Overly large depth limit (defeats purpose of IntroSort)
    return inefficient_intro_sort_helper(arr, 0, len(arr) - 1, max_depth)

def inefficient_intro_sort_helper(arr, low, high, depth_limit):
    if low < high:
        if depth_limit == 0:
            # WORST switch to HeapSort (sorts full array instead of subarray)
            arr[:] = inefficient_heap_sort(arr)
            return arr
        
        # WORST pivot selection: Always picking first element (bad for sorted input)
        pivot = arr[low]
        partition_index = inefficient_partition(arr, low, high, pivot)
        
        # Overly deep recursive calls
        inefficient_intro_sort_helper(arr, low, partition_index - 1, depth_limit - 1)
        inefficient_intro_sort_helper(arr, partition_index + 1, high, depth_limit - 1)

    # WORST case: Unnecessary call to Insertion Sort at the end even if sorted
    return inefficient_insertion_sort(arr)

# Inefficient partition function (bad pivoting & excessive swaps)
def inefficient_partition(arr, low, high, pivot):
    left = []
    right = []
    
    # Instead of partitioning in-place, we create two extra lists
    for i in range(low, high + 1):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    # WORST way: Copy everything back instead of swapping
    arr[low:high + 1] = left + right  
    return len(left) + low  # Incorrect partition index

# Inefficient HeapSort (already bad, as seen before)
def inefficient_heap_sort(arr):
    heap = []
    for num in arr:
        heapq.heappush(heap, num)  # Uses unnecessary heap memory

    sorted_arr = []
    while heap:
        sorted_arr.append(heapq.heappop(heap))

    return sorted_arr  # Pointless copying

# Inefficient Insertion Sort (slowest possible version)
def inefficient_insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]  # Swap instead of shifting
            j -= 1
    return arr[:]  # Unnecessary list copy


random.seed(0)
L_size = 10000 # int to pass to range
L = []
for _ in range(L_size):
    num = random.random() # create random num and append
    L.append(num)

inefficient_intro_sort(L)
