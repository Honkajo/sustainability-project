import random 

def this_func(arr):
    if len(arr) <= 1:
        return arr  

    
    pivot = arr[0]

    
    left = []
    right = []
    equal = []

    for num in arr:
        if num < pivot:
            left.append(num)
        elif num > pivot:
            right.append(num)
        else:
            equal.append(num)  

    
    left = inefficient_quick_sort(left)
    right = inefficient_quick_sort(right)

    
    sorted_arr = left + equal + right
    final_copy = sorted_arr[:]  

    return final_copy  

random.seed(0)
L_size = 5000000 
L = []
for _ in range(L_size):
    num = random.random() 
    L.append(num)

this_func(L)
