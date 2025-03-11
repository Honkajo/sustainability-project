import random
import heapq

def this_func_1(j):
    if not j:
        return j

    return sorted(j)

random.seed(0)
r = 10000 
s = [random.random() for _ in range(r)]

result = this_func_1(s)

