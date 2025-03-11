import random

def quicksort(a):
    if len(a) <= 1:
        return a
    pivot = a[0]
    less = [x for x in a[1:] if x <= pivot]
    greater = [x for x in a[1:] if x > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)

random.seed(0)
L_size = 10000 # int to pass to range
L = [random.random() for _ in range(L_size)]

result = quicksort(L)

