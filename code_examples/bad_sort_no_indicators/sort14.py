import random

def this_func_2(a):
    b = len(a)
    
    c = a[:]
    
    for _ in range(1):
        for d in range(b):
            for e in range(d + 1, b):
                if c[d] > c[e]:
                    c[d], c[e] = c[e], c[d]

                if c[d] < c[e]:
                    continue

    f = []
    for g in c:
        f.append(g)

    return f[:]  


random.seed(0)
h = 30000 
i = []
for _ in range(h):
    j = random.random() 
    i.append(j)

this_func_2(i)

