import random

def smoothsort(arr):
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < n and arr[largest] < arr[left]:
            largest = left
        if right < n and arr[largest] < arr[right]:
            largest = right
        
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)
    
    n = len(arr)
    
    # Step 1: Build the heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Step 2: Extract elements from heap
    sorted_arr = []
    while arr:
        arr[0], arr[-1] = arr[-1], arr[0]
        sorted_arr.append(arr.pop())
        heapify(arr, len(arr), 0)
    
    return sorted_arr

random.seed(0)
L_size = 20000  # Size of the list
L = [random.random() for _ in range(L_size)]  # Generate list of random numbers

smoothsort(L)

