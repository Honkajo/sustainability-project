import random

def optimized_merge_sort(arr):
    if len(arr) <= 1:
        return arr  # Base case

    # Optimized midpoint calculation: directly use integer division
    mid = len(arr) // 2

    # Slice the list into two halves
    left = arr[:mid]
    right = arr[mid:]

    # Recursively sort the partitions
    left = optimized_merge_sort(left)
    right = optimized_merge_sort(right)

    # Efficient merge process using two pointers
    return optimized_merge(left, right)

def optimized_merge(left, right):
    sorted_list = []
    i, j = 0, 0

    # Merge the two sorted lists
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    # Append remaining elements if any
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list

random.seed(0)
L_size = 300000  # Adjust the size of the list
L = [random.random() for _ in range(L_size)]  # Efficient list initialization

optimized_merge_sort(L)

