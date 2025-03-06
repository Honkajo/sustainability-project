def function_p_f_z_optimized(n):
    factors = []
    
    # Check for factors up to the square root of n
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors.append(i)
            if i != n // i:  # Avoid adding the square root twice
                factors.append(n // i)
    
    return sorted(factors)

# Example usage
n = 1234
result = function_p_f_z_optimized(n)
print(result)

