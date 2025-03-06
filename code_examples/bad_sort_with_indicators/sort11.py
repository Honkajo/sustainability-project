import random

def inefficient_selection_sort(arr):
    n = len(arr)

    # WORST way: Create an extra list and copy elements
    temp_arr = arr[:]
    
    for i in range(n):
        # WORST way to find the minimum: Iterate multiple times
        min_index = i
        for j in range(i + 1, n):
            if temp_arr[j] < temp_arr[min_index]:
                min_index = j
        
        # WORST way to swap: Create unnecessary temporary variables
        if min_index != i:
            a, b = temp_arr[i], temp_arr[min_index]
            temp_arr[i], temp_arr[min_index] = b, a  # Useless variable assignment

        # Extra pointless loop to "simulate" a deep copy
        temp_copy = []
        for num in temp_arr:
            temp_copy.append(num)
        temp_arr = temp_copy[:]  # Another redundant copy

    return temp_arr[:]  # Final useless copy before returning

random.seed(0)
L_size = 20000 # int to pass to range
L = []
for _ in range(L_size):
    num = random.random() # create random num and append
    L.append(num)

inefficient_selection_sort(L)
