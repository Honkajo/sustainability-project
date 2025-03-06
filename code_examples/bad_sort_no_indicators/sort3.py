import random

def this_func(arr):
    n = len(arr)
    for i in range(n):
        swapped = False  
        for j in range(n - 1): 
            if arr[j] > arr[j + 1]:  
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  
                swapped = True  
        
        
        if not swapped:
            for k in range(n):
                pass 
        
            swapped = True

    return arr

random.seed(0)
L_size = 10000 
L = []
for _ in range(L_size):
    num = random.random() 

this_func(L)
