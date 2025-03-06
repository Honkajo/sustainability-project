import random

def inefficient_sample_sort(arr, num_pivots=3):
    if len(arr) <= 1:
        return arr  # Base case

    # WORST way: Selecting pivots randomly and sorting them unnecessarily
    pivot_candidates = random.sample(arr, min(num_pivots, len(arr)))  
    pivot_candidates.sort()  # Unnecessary sorting operation

    # WORST way to distribute elements into partitions (extra loops & copying)
    partitions = [[] for _ in range(len(pivot_candidates) + 1)]
    
    for num in arr:
        for i, pivot in enumerate(pivot_candidates):
            if num < pivot:
                partitions[i].append(num)
                break
        else:
            partitions[-1].append(num)

    # Extra useless copying of partitions
    temp_partitions = [part[:] for part in partitions]

    # Overly deep recursive calls
    sorted_partitions = [inefficient_sample_sort(part) for part in temp_partitions]

    # WORST way: Manually concatenate everything (wasting memory)
    sorted_arr = []
    for part in sorted_partitions:
        for num in part:
            sorted_arr.append(num)

    return sorted_arr[:]  # Final redundant copy before returning


random.seed(0)
L_size = 2000000 # int to pass to range
L = []
for _ in range(L_size):
    num = random.random() # create random num and append
    L.append(num)

inefficient_sample_sort(L)
