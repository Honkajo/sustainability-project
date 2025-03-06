def efficient_prime_finder(limit):
    sieve = [True] * (limit + 1)
    sieve[0], sieve[1] = False, False  # 0 and 1 are not prime numbers

    for num in range(2, int(limit ** 0.5) + 1):  # Only go up to sqrt(limit)
        if sieve[num]:
            for multiple in range(num * num, limit + 1, num):  # Mark all multiples as non-prime
                sieve[multiple] = False

    # Extracting the primes from the sieve
    primes = [num for num, is_prime in enumerate(sieve) if is_prime]
    return primes

# Example usage
primes = efficient_prime_finder(2000)

