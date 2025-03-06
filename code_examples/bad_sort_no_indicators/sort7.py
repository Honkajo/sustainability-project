import random 

def this_func_1(a):
    b = len(a)

    for _ in range(b):
        for c in range(1, b):
            d = c
            while d > 0 and a[d] < a[d - 1]:
                a[d], a[d - 1] = a[d - 1], a[d]
                d -= 1

        e = []
        for f in a:
            e.append(f)
        a = e[:]  

    return a[:]


random.seed(0)
g = 10000 
h = []
for _ in range(g):
    i = random.random() 
    h.append(i)

this_func_1(h)
