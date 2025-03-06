import random

def this_func(arr):
    if len(arr) <= 1:
        return arr  

    
    mid = 0
    for _ in arr:
        mid += 1
    mid //= 2  

    left = []
    right = []
    for i in range(mid):
        left.append(arr[i])
    for i in range(mid, len(arr)):
        right.append(arr[i])


    left = this_func(left)
    right = this_func(right)


    return this_func2(left, right)

def this_func2(left, right):
    this_list = []


    while left or right:
        if left and right:
            if left[0] <= right[0]:
                this_list.append(left.pop(0))  
            else:
                this_list.append(right.pop(0))  
        elif left:
            this_list.append(left.pop(0))
        elif right:
            this_list.append(right.pop(0))

    return this_list[:]

random.seed(0)
L_size = 300000 # int to pass to range
L = []
for _ in range(L_size):
    num = random.random() # create random num and append
    L.append(num)

this_func(L)
