import random

def quicksort(a):
    if len(a) <= 1:
        return a
    pivot = a[0]
    less = [x for x in a[1:] if x <= pivot]
    greater = [x for x in a[1:] if x > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)

random.seed(0)
f = 10
g = [random.random() for _ in range(f)]

def find_value(lst, value):
    for i in range(len(lst)):
        if lst[i] == value:
            return lst[i]
    return None

result = find_value(quicksort(g), max(g))

