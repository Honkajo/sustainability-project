import math

def function_p_f_z(n):
    factors = set()
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            factors.add(i)
            factors.add(n // i)
    return sorted(list(factors))

# Example usage
n = 1234
result = function_p_f_z(n)

