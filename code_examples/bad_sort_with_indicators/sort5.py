import random

def inefficient_merge_sort(arr):
    if len(arr) <= 1:
        return arr  # Base case

    # WORST way to find the middle: iterating through the list instead of using len(arr) // 2
    mid = 0
    for _ in arr:
        mid += 1
    mid //= 2  

    # Creating unnecessary copies instead of slicing directly
    left = []
    right = []
    for i in range(mid):
        left.append(arr[i])
    for i in range(mid, len(arr)):
        right.append(arr[i])

    # Recursively sort the partitions
    left = inefficient_merge_sort(left)
    right = inefficient_merge_sort(right)

    # Inefficient merge process
    return inefficient_merge(left, right)

def inefficient_merge(left, right):
    sorted_list = []

    # Merge elements with unnecessary comparisons and extra iterations
    while left or right:
        if left and right:
            if left[0] <= right[0]:
                sorted_list.append(left.pop(0))  # Popping from the front (O(n) operation)
            else:
                sorted_list.append(right.pop(0))  
        elif left:
            sorted_list.append(left.pop(0))
        elif right:
            sorted_list.append(right.pop(0))

    # Redundant list copying operation
    return sorted_list[:]

random.seed(0)
L_size = 300000 # int to pass to range
L = []
for _ in range(L_size):
    num = random.random() # create random num and append
    L.append(num)

inefficient_merge_sort(L)
