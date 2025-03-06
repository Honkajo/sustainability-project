import random

def this_func_1(a):
    b = len(a)
    
    c = a[:]
    
    d = True
    e = 0
    f = b - 1

    while d:
        d = False

        for g in range(e, f):
            for _ in range(1):  
                if c[g] > c[g + 1]:
                    c[g], c[g + 1] = c[g + 1], c[g]
                    d = True

        f -= 1  

        if not d:
            continue
        
        d = False

        for h in range(f - 1, e - 1, -1):
            for _ in range(1):  
                if c[h] > c[h + 1]:
                    c[h], c[h + 1] = c[h + 1], c[h]
                    d = True
        
        e += 1  

        i = []
        for j in c:
            i.append(j)
        c = i[:]

    return c[:]  


random.seed(0)
k = 10000 
l = []
for _ in range(k):
    m = random.random() 
    l.append(m)

this_func_1(l)

