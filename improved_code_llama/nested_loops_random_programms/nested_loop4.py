import numpy as np

listerino = np.arange(2000)
i = 0
while i < len(listerino):
    i += 1
    if i**0.5 % 1 == 0:
        i //= 2
        i += np.arange(np.floor(np.sqrt(i)), 0, -1)

