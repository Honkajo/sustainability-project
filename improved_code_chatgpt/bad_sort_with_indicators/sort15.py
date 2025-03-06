import random

def bogosort(arr):
    while not is_sorted(arr):
        random.shuffle(arr)  # Just shuffle once instead of twice
    return arr  # No need to copy the array unnecessarily

# Check if the array is sorted
def is_sorted(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

random.seed(0)
L_size = 10  # Small array size for demonstration
L = [random.random() for _ in range(L_size)]

bogosort(L)

