import random

def optimized_sample_sort(arr, num_pivots=3):
    if len(arr) <= 1:
        return arr  # Base case

    # Select pivots randomly without sorting
    pivot_candidates = random.sample(arr, min(num_pivots, len(arr)))  

    # Distribute elements into partitions based on pivots
    partitions = [[] for _ in range(len(pivot_candidates) + 1)]

    for num in arr:
        # Determine which partition the number belongs to
        placed = False
        for i, pivot in enumerate(pivot_candidates):
            if num < pivot:
                partitions[i].append(num)
                placed = True
                break
        if not placed:
            partitions[-1].append(num)

    # Recursively sort each partition and concatenate the results
    sorted_arr = []
    for part in partitions:
        sorted_arr.extend(optimized_sample_sort(part))

    return sorted_arr

random.seed(0)
L_size = 2000000 # int to pass to range
L = [random.random() for _ in range(L_size)]

optimized_sample_sort(L)

