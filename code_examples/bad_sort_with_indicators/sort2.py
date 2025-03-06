import random

random.seed(0)
L_size = 10000 # int to pass to range
L = []
for _ in range(L_size):
    num = random.random() # create random num and append
    L.append(num)

def bad_bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-1):
            if arr[j] > arr[j+1]:  # Always swapping even if unnecessary
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

bad_bubble_sort(L)
