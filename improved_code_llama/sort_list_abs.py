import random

random.seed(0)
L_size = 2000000 
L = [random.random() for _ in range(L_size)]

newL = sorted(L, key=abs, reverse=True)

