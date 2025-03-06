import random

def optimized_insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # Shift elements to the right
            j -= 1
        arr[j + 1] = key  # Insert the key in the correct position
    return arr

random.seed(0)
L_size = 10000  # Adjust the size of the list
L = [random.random() for _ in range(L_size)]  # Efficient list initialization

optimized_insertion_sort(L)

