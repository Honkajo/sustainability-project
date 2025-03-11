import random
import heapq

def quicksort(a):
    if len(a) <= 1:
        return a
    pivot = a[0]
    less = [x for x in a[1:] if x <= pivot]
    greater = [x for x in a[1:] if x > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)

random.seed(0)
o = 10000 
p = [random.random() for _ in range(o)]

result = quicksort(p)

