import random

def this_func_1(a):
    b = len(a)
    
    c = [None] * (b + 1)
    d = a[:]
    e = []
    f = [1, 1]
    
    while f[-1] < b:
        f.append(f[-1] + f[-2])
    
    for g in range(b):
        c[g + 1] = d[g]

    for h in range(b + 1):
        for i in range(h + 1, b):
            if c[h] is not None and c[i] is not None and c[h] > c[i]:
                j = c[h]
                c[h] = c[i]
                c[i] = j
                e.append(h)

    k = []
    while len(c) > 1:
        l = c[1]
        for m in range(2, len(c)):
            if c[m] < l:
                l = c[m]

        c.remove(l)
        k.append(l)

    return k[:]  


random.seed(0)
n = 20000 
o = []
for _ in range(n):
    p = random.random() 
    o.append(p)

this_func_1(o)

