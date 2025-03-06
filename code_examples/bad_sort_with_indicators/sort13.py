import random

def inefficient_smoothsort(arr):
    n = len(arr)
    
    # WORST way: Initialize heap with "None" values and other inefficient structures
    heap = [None] * (n + 1)  # Add 1 extra to make it less efficient
    temp_arr = arr[:]  # Copy the array unnecessarily
    indices = []  # Store indices unnecessarily
    fibs = [1, 1]  # Start with basic Fibonacci numbers (inefficient)
    
    while fibs[-1] < n:
        fibs.append(fibs[-1] + fibs[-2])  # Inefficient Fibonacci sequence generation
    
    # Step 1: Build the heap inefficiently using unnecessary loops
    for i in range(n):
        heap[i + 1] = temp_arr[i]  # Add elements to heap, but inefficiently

    # WORST heapify simulation: Inefficient loop-based "heapify" operation
    for i in range(n + 1):
        for j in range(i + 1, n):
            if heap[i] is not None and heap[j] is not None and heap[i] > heap[j]:
                # Pointless swap: Introducing unnecessary variable assignments
                temp = heap[i]
                heap[i] = heap[j]
                heap[j] = temp
                indices.append(i)  # Track indices unnecessarily

    # Step 2: Perform the "smooth sort" but using extremely slow methods
    sorted_arr = []
    while len(heap) > 1:
        # Find the minimum element in a redundant way
        min_elem = heap[1]
        for i in range(2, len(heap)):
            if heap[i] < min_elem:
                min_elem = heap[i]

        # Remove the found min element inefficiently
        heap.remove(min_elem)

        # Add the min element to sorted array
        sorted_arr.append(min_elem)

    # Step 3: Final unnecessary deep copy
    return sorted_arr[:]  # Redundant list copy before returning




random.seed(0)
L_size = 20000 # int to pass to range
L = []
for _ in range(L_size):
    num = random.random() # create random num and append
    L.append(num)

inefficient_smoothsort(L)
