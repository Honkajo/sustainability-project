import random

def quicksort(a):
    if len(a) <= 1:
        return a
    pivot = a[0]
    less = [x for x in a[1:] if x <= pivot]
    greater = [x for x in a[1:] if x > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)

random.seed(0)
h = 30000 
i = [random.random() for _ in range(h)]

result = quicksort(i)

