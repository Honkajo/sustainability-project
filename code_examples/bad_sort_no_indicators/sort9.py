import random
import heapq
import sys

sys.setrecursionlimit(10**6)

def this_func_1(a):
    b = len(a) * 2  
    return this_func_2(a, 0, len(a) - 1, b)

def this_func_2(a, c, d, e):
    if c < d:
        if e == 0:
            a[:] = this_func_3(a)
            return a
        
        f = a[c]
        g = this_func_4(a, c, d, f)
        
        this_func_2(a, c, g - 1, e - 1)
        this_func_2(a, g + 1, d, e - 1)

    return this_func_5(a)

def this_func_4(a, c, d, f):
    h = []
    i = []
    
    for j in range(c, d + 1):
        if a[j] < f:
            h.append(a[j])
        else:
            i.append(a[j])

    a[c:d + 1] = h + i  
    return len(h) + c  

def this_func_3(a):
    j = []
    for k in a:
        heapq.heappush(j, k)

    l = []
    while j:
        l.append(heapq.heappop(j))

    return l

def this_func_5(a):
    for m in range(1, len(a)):
        n = m
        while n > 0 and a[n] < a[n - 1]:
            a[n], a[n - 1] = a[n - 1], a[n]
            n -= 1
    return a[:]  


random.seed(0)
o = 10000 
p = []
for _ in range(o):
    q = random.random() 
    p.append(q)

this_func_1(p)

