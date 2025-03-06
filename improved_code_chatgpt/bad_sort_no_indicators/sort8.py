import random
import heapq

def this_func_1(j):
    if not j:
        return j

    heapq.heapify(j)  # O(n) heap construction
    return [heapq.heappop(j) for _ in range(len(j))]  # O(n log n) sorting

random.seed(0)
r = 10_000  
s = [random.random() for _ in range(r)]  # Faster list creation

this_func_1(s)

