import random
import heapq

def optimized_heap_sort(arr):
    if not arr:
        return arr  # Base case check

    heapq.heapify(arr)  # Transform the list into a heap in-place
    sorted_arr = []

    # Pop elements from the heap and append them to the sorted array
    while arr:
        min_element = heapq.heappop(arr)
        sorted_arr.append(min_element)

    return sorted_arr  # Return the sorted array directly

random.seed(0)
L_size = 10000  # Adjust size based on requirements
L = [random.random() for _ in range(L_size)]  # Efficient list initialization

optimized_heap_sort(L)

