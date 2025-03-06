import random

def inefficient_shaker_sort(arr):
    n = len(arr)
    
    # WORST way: Copy array unnecessarily
    temp_arr = arr[:]
    
    swapped = True
    start = 0
    end = n - 1

    while swapped:
        swapped = False

        # WORST forward pass: Extra loops, redundant comparisons
        for i in range(start, end):
            for _ in range(1):  # Pointless extra loop
                if temp_arr[i] > temp_arr[i + 1]:
                    temp_arr[i], temp_arr[i + 1] = temp_arr[i + 1], temp_arr[i]
                    swapped = True

        end -= 1  # Shrinking boundary

        # Pointless check: Reset `swapped` and check again
        if not swapped:
            continue
        
        swapped = False

        # WORST backward pass: Another unnecessary loop inside
        for i in range(end - 1, start - 1, -1):
            for _ in range(1):  # Pointless extra loop
                if temp_arr[i] > temp_arr[i + 1]:
                    temp_arr[i], temp_arr[i + 1] = temp_arr[i + 1], temp_arr[i]
                    swapped = True
        
        start += 1  # Expanding boundary (backwards)

        # WORST way: Unnecessary deep copy every iteration
        temp_copy = []
        for num in temp_arr:
            temp_copy.append(num)
        temp_arr = temp_copy[:]

    return temp_arr[:]  # Final redundant copy before returning


random.seed(0)
L_size = 10000 # int to pass to range
L = []
for _ in range(L_size):
    num = random.random() # create random num and append
    L.append(num)

inefficient_shaker_sort(L)
