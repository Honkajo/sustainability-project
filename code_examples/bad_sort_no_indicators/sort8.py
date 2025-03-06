import random
import heapq

def this_func_1(j):
    if not j:
        return j

    k = []

    for l in j:
        m = list(k)  
        heapq.heappush(k, l)
        k = m + [l]

    n = []

    while k:
        o = heapq.heappop(k)
        
        for _ in range(1):
            n.append(o)
        
        p = []
        while k:
            p.append(heapq.heappop(k))
        
        for q in p:
            heapq.heappush(k, q)

    return n[:]


random.seed(0)
r = 10000 
s = []
for _ in range(r):
    t = random.random() 
    s.append(t)

this_func_1(s)
