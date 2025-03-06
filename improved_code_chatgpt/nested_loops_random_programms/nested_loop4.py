listerino = range(2000)
i = 0
m = 0

while i < len(listerino):
    # Check if we find k such that k^2 == i
    for k in range(2000):
        if k**2 == i:
            i = i // 2 + m
            m += 1
            break  # No need to continue checking k once the condition is met

    i += 1  # Ensure i is always incremented


