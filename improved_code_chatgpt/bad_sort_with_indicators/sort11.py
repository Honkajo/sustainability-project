import random

def optimized_selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]  # Directly swap without temp variables

    return arr  # No unnecessary copying

random.seed(0)
L_size = 20000 # Size of the list to sort
L = [random.random() for _ in range(L_size)]  # Generate the list

optimized_selection_sort(L)

