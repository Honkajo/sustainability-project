def efficient_prime_finder(limit):
    # Create a boolean array to mark primes
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes

    # Sieve of Eratosthenes
    for num in range(2, int(limit**0.5) + 1):
        if is_prime[num]:
            for multiple in range(num * num, limit + 1, num):
                is_prime[multiple] = False

    # Collect all prime numbers
    primes = [num for num, prime in enumerate(is_prime) if prime]
    return primes

# Example usage
primes = efficient_prime_finder(2000)

