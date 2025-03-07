import random

def sample_sort(arr, num_pivots=3):
    if len(arr) <= 1:
        return arr  # Base case

    pivot_candidates = random.sample(arr, min(num_pivots, len(arr)))
    sorted_arr = []

    for num in arr:
        for pivot in pivot_candidates:
            if num < pivot:
                sorted_arr.append(num)
                break
        else:
            sorted_arr.append(num)

    return sorted_arr


random.seed(0)
L_size = 2000000 
L = [random.random() for _ in range(L_size)]

result = sample_sort(L)

