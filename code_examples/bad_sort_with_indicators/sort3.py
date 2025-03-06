import random

def inefficient_bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False  # A flag to check if any swapping happened
        for j in range(n - 1):  # Instead of reducing comparisons, we always loop fully
            if arr[j] > arr[j + 1]:  
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap
                swapped = True  
        
        # Introducing unnecessary iteration even if the array is sorted
        if not swapped:  
            for k in range(n):
                pass  # Just looping for no reason
        
        # Reset swapped manually instead of breaking
        swapped = True  

    return arr

random.seed(0)
L_size = 10000 # int to pass to range
L = []
for _ in range(L_size):
    num = random.random() # create random num and append
    L.append(num)

inefficient_bubble_sort(L)
