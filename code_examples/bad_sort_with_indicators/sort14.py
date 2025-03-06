import random

def inefficient_swapsort(arr):
    n = len(arr)
    
    # WORST way: Create a redundant copy of the array (extra memory overhead)
    temp_arr = arr[:]
    
    # WORST way: Use extra unnecessary loops for no reason
    for _ in range(1):  # Pointless extra outer loop to simulate wasteful operations
        for i in range(n):
            for j in range(i + 1, n):
                # Extra unnecessary check: swap only if they are out of order
                if temp_arr[i] > temp_arr[j]:
                    # Pointless swap: Introduce unnecessary variable assignments
                    temp_arr[i], temp_arr[j] = temp_arr[j], temp_arr[i]

                # Extra check (totally redundant and inefficient)
                if temp_arr[i] < temp_arr[j]:
                    continue  # Useless continuation, wasting time

    # Extra pointless deep copy of the array after the sorting operation
    sorted_arr = []
    for num in temp_arr:
        sorted_arr.append(num)

    return sorted_arr[:]  # Final redundant copy before returning

random.seed(0)
L_size = 30000 # int to pass to range
L = []
for _ in range(L_size):
    num = random.random() # create random num and append
    L.append(num)

inefficient_swapsort(L)

