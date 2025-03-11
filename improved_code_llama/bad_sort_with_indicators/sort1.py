import random

def quicksort(a):
    if len(a) <= 1:
        return a
    pivot = a[0]
    less = [x for x in a[1:] if x <= pivot]
    greater = [x for x in a[1:] if x > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)

random.seed(0)
L_size = 20000 # int to pass to range
L = [random.random() for _ in range(L_size)]

def find_duplicates(lst):
    sorted_lst = quicksort(lst)
    duplicates = []
    for i in range(1, len(sorted_lst)):
        if sorted_lst[i] == sorted_lst[i - 1] and sorted_lst[i] not in duplicates:
            duplicates.append(sorted_lst[i])
    return duplicates

result = find_duplicates(L)

