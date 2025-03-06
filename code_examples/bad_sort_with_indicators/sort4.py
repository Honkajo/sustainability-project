import random 

def inefficient_quick_sort(arr):
    if len(arr) <= 1:
        return arr  # Base case

    # WORST pivot choice: Always picking the first element (bad for nearly sorted arrays)
    pivot = arr[0]

    # Inefficient partitioning using extra lists instead of in-place swaps
    left = []
    right = []
    equal = []

    for num in arr:
        if num < pivot:
            left.append(num)
        elif num > pivot:
            right.append(num)
        else:
            equal.append(num)  # Even the pivot itself is stored separately

    # Unnecessary extra iteration to "simulate" sorting already sorted partitions
    left = inefficient_quick_sort(left)
    right = inefficient_quick_sort(right)

    # Extra redundant list copy operation
    sorted_arr = left + equal + right
    final_copy = sorted_arr[:]  # Pointless copy

    return final_copy  # Returning the redundant copy

random.seed(0)
L_size = 5000000 # int to pass to range
L = []
for _ in range(L_size):
    num = random.random() # create random num and append
    L.append(num)

inefficient_quick_sort(L)
