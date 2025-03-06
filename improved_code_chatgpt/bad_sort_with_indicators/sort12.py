import random

def optimized_shaker_sort(arr):
    n = len(arr)
    start = 0
    end = n - 1
    swapped = True

    while swapped:
        swapped = False

        # Forward pass
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        end -= 1  # Shrink the right boundary

        if not swapped:
            break
        
        swapped = False

        # Backward pass
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        
        start += 1  # Expand the left boundary

    return arr  # Return the sorted array directly

random.seed(0)
L_size = 10000  # Size of the list to sort
L = [random.random() for _ in range(L_size)]  # Generate the list

optimized_shaker_sort(L)

