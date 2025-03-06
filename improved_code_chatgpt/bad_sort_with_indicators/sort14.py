import random

def swap_sort(arr):
    n = len(arr)
    
    # Simple swap sort: Repeatedly swap out-of-order adjacent elements
    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap out-of-order elements
                
    return arr

random.seed(0)
L_size = 30000  # Size of the list
L = [random.random() for _ in range(L_size)]  # Generate list of random numbers

swap_sort(L)

