import random
from collections import deque

def this_func(arr):
    if len(arr) <= 1:
        return arr  

    mid = len(arr) // 2
    left = this_func(arr[:mid])
    right = this_func(arr[mid:])

    return this_func2(left, right)

def this_func2(left, right):
    left, right = deque(left), deque(right)  # Convert to deque for O(1) pops
    merged_list = []

    while left and right:
        if left[0] <= right[0]:
            merged_list.append(left.popleft())  
        else:
            merged_list.append(right.popleft())  

    merged_list.extend(left)
    merged_list.extend(right)

    return merged_list  # No need for [:]

random.seed(0)
L_size = 300_000  # Use underscores for readability
L = [random.random() for _ in range(L_size)]  # Efficient list creation

this_func(L)

