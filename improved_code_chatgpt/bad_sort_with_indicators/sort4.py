import random

def optimized_quick_sort(arr):
    if len(arr) <= 1:
        return arr  # Base case, no sorting needed

    # Improved pivot selection: Median of three (first, middle, last)
    first, middle, last = arr[0], arr[len(arr) // 2], arr[-1]
    pivot = sorted([first, middle, last])[1]  # Median of three pivot selection
    
    # In-place partitioning: No extra space needed for left and right lists
    left, right = [], []
    
    for num in arr[1:]:  # Skip the pivot itself (already chosen)
        if num < pivot:
            left.append(num)
        else:
            right.append(num)

    # Recursively sort left and right subarrays
    return optimized_quick_sort(left) + [pivot] + optimized_quick_sort(right)

random.seed(0)
L_size = 5000000  # Size of the list
L = [random.random() for _ in range(L_size)]  # Efficient list initialization

optimized_quick_sort(L)

