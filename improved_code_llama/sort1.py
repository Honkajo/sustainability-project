import random

random.seed(0)
L_size = 20000 
L = [random.random() for _ in range(L_size)]

def find_duplicates(lst):
    return list(set([x for x in lst if lst.count(x) > 1]))

find_duplicates(L)

