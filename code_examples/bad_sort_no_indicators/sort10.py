import random

def this_func_1(a, b=3):
    if len(a) <= 1:
        return a

    c = random.sample(a, min(b, len(a)))
    c.sort()

    d = [[] for _ in range(len(c) + 1)]
    
    for e in a:
        for f, g in enumerate(c):
            if e < g:
                d[f].append(e)
                break
        else:
            d[-1].append(e)

    h = [i[:] for i in d]

    i = [this_func_1(j) for j in h]

    j = []
    for k in i:
        for l in k:
            j.append(l)

    return j[:]  


random.seed(0)
m = 2000000 
n = []
for _ in range(m):
    o = random.random() 
    n.append(o)

this_func_1(n)

