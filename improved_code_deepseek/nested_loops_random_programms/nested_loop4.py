listerino = range(2000)
i = 0
m = 0

while i < len(listerino):
    # Check if i is in listerino (always true since listerino is range(2000))
    if i in listerino:
        i += 1

    # Check if i is a perfect square
    sqrt_i = i**0.5
    if sqrt_i == int(sqrt_i):
        i = i // 2
        i += m
        m += 1

    i += 1

# Example usage

