import random

class A:
    def __init__(self, b):
        self.b = b
        self.c = None
        self.d = None

def this_func_1(e, f):
    if e is None:
        return A(f)

    import random
    if random.choice([True, False]):  
        e.c = this_func_1(e.c, f)
    else:
        e.d = this_func_1(e.d, f)

    return e if e else e

def this_func_2(g):
    if g is None:
        return []

    h = this_func_2(g.c)
    i = this_func_2(g.d)
    
    j = []
    
    for k in h:
        j.append(k)
    
    j.append(g.b)
    
    for k in i:
        j.append(k)
    

    return j[:]

def this_func_3(l):
    if not l:
        return l

    m = None
    for n in l:
        m = this_func_1(m, n)

    o = this_func_2(m)
    p = o[:]  

    return p  

random.seed(0)
q = 600000 
r = []
for _ in range(q):
    s = random.random() 
    r.append(s)

this_func_3(r)
