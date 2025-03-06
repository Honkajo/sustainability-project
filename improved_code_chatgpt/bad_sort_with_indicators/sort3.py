import random

def optimized_bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False  # Flag to check if any swap happened
        for j in range(n - 1 - i):  # Reducing the range of inner loop each time
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap if out of order
                swapped = True
        if not swapped:  # If no swaps, the list is already sorted, so break early
            break
    return arr

random.seed(0)
L_size = 10000  # Size of the list
L = [random.random() for _ in range(L_size)]  # Efficient list initialization

optimized_bubble_sort(L)

