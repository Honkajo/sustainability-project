listerino = range(2000)
i = 0
m = 0
while i < len(listerino):
    for j in listerino:
        if j == i:
            i += 1
            break
    for k in range(2000):
        if k**2 == i:
            i = i//2
            i += m
            m += 1
    i += 1

