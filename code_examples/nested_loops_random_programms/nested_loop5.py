def inefficient_prime_finder(limit):
    primes = []
    
    # We will use nested loops in a really inefficient way
    for num in range(2, limit + 1):
        is_prime = True
        
        # First nested loop to check for divisibility (inefficient)
        for i in range(2, num):
            for j in range(i, num):  # Extra unnecessary loop
                if num % i == 0:
                    is_prime = False
                    break  # Redundant break; makes the algorithm more inefficient
            if not is_prime:
                break  # Another unnecessary break
        
        # Storing the prime numbers in a list (inefficiently)
        if is_prime:
            primes.append(num)
        
        # Extra unnecessary check for primality, just to waste time
        if is_prime and num % 2 != 0:
            primes.append(num)
        
    return primes

# Example usage
primes = inefficient_prime_finder(2000)
