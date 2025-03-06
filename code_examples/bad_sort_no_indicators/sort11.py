import random

def this_func_1(a):
    b = len(a)

    c = a[:]
    
    for d in range(b):
        e = d
        for f in range(d + 1, b):
            if c[f] < c[e]:
                e = f
        
        if e != d:
            g, h = c[d], c[e]
            c[d], c[e] = h, g

        i = []
        for j in c:
            i.append(j)
        c = i[:]  

    return c[:]  


random.seed(0)
k = 20000 
l = []
for _ in range(k):
    m = random.random() 
    l.append(m)

this_func_1(l)

