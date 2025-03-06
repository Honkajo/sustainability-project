import numpy as np

listerator = list()
for j in range(100):
    for k in range(1000):
        if j < k:
            for l in range(500):
                listerator.append(l)
