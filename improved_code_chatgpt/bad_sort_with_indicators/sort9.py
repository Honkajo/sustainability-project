import random
import heapq
import sys

def optimized_intro_sort(arr):
    max_depth = len(arr) * 2  # Proper depth limit for introsort
    return optimized_intro_sort_helper(arr, 0, len(arr) - 1, max_depth)

def optimized_intro_sort_helper(arr, low, high, depth_limit):
    if low < high:
        if depth_limit == 0:
            # Switch to heapsort if recursion depth limit is reached
            heap_sort(arr)
            return arr
        
        # Choose pivot using median of three or random pivot
        pivot = median_of_three(arr, low, high)
        partition_index = partition(arr, low, high, pivot)
        
        optimized_intro_sort_helper(arr, low, partition_index - 1, depth_limit - 1)
        optimized_intro_sort_helper(arr, partition_index + 1, high, depth_limit - 1)

    return arr

def partition(arr, low, high, pivot):
    left = low
    right = high
    while True:
        while arr[left] < pivot:
            left += 1
        while arr[right] > pivot:
            right -= 1
        if left >= right:
            return right
        arr[left], arr[right] = arr[right], arr[left]
    return right

def median_of_three(arr, low, high):
    mid = (low + high) // 2
    a, b, c = arr[low], arr[mid], arr[high]
    if a > b:
        if b > c:
            pivot = b
        elif a > c:
            pivot = a
        else:
            pivot = c
    else:
        if a > c:
            pivot = a
        elif b > c:
            pivot = b
        else:
            pivot = c
    return pivot

def heap_sort(arr):
    heapq.heapify(arr)  # Transform the list into a heap in-place
    sorted_arr = [heapq.heappop(arr) for _ in range(len(arr))]
    return sorted_arr

random.seed(0)
L_size = 10000
L = [random.random() for _ in range(L_size)]

optimized_intro_sort(L)

