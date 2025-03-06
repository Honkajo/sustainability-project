def function_p_f_z(n):
    factors = []
    for i in range(2, n + 1):
        for j in range(2, i + 1):
            for k in range(2, j + 1):
                if i % j == 0 and n % i == 0:
                    factors.append(i)
                    break
    return factors

# Example usage
n = 1234
result = function_p_f_z(n)
print(result)

