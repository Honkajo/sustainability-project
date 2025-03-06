import random

random.seed(0)
L_size = 2000000 # int to pass to range
L = []
for _ in range(L_size):
    num = random.random() # create random num and append
    L.append(num)


newL = sorted(L, key=abs, reverse=True)
