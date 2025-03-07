def efficient_prime_factors(n):
    factors = []
    
    # Check for the number of 2s that divide n
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    
    # n must be odd at this point, so a skip of 2 (i.e., i = i +2) can be used
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i
    
    # This condition is to check if n is a prime number greater than 2
    if n > 2:
        factors.append(n)
    
    return factors

# Example usage
n = 1234
result = efficient_prime_factors(n)

