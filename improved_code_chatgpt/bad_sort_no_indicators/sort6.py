import random

class A:
    def __init__(self, b):
        self.b = b
        self.c = None
        self.d = None

def this_func_1(e, f):
    if e is None:
        return A(f)

    if f < e.b:  # Keep tree structured (Binary Search Tree)
        e.c = this_func_1(e.c, f)
    else:
        e.d = this_func_1(e.d, f)

    return e  

def this_func_2(g):
    if g is None:
        return []

    # Use extend() instead of multiple appends
    return this_func_2(g.c) + [g.b] + this_func_2(g.d)

def this_func_3(l):
    if not l:
        return []

    m = None
    for n in l:
        m = this_func_1(m, n)

    return this_func_2(m)  # No need for list copying

random.seed(0)
q = 600_000  # Use underscore for readability
r = [random.random() for _ in range(q)]  # Faster list creation

this_func_3(r)

