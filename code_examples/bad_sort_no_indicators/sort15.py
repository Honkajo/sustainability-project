import random

def this_func_3(a):
    b = len(a)
    
    c = a[:]
    
    for _ in range(1):
        while not z(c):
            random.shuffle(c)
            c = random.sample(c, b)
            c = c[::-1]
            
            if z(c):
                break
    
    d = []
    for e in c:
        d.append(e)
    
    return d[:]  

def z(a):
    for b in range(1, len(a)):
        if a[b - 1] > a[b]:
            return False
    return True


random.seed(0)
f = 10
g = []
for _ in range(f):
    h = random.random()
    g.append(h)

this_func_3(g)

