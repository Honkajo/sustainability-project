def efficient_fibonacci(n):
    fib = []
    a, b = 0, 1  # Initialize the first two Fibonacci numbers
    
    for _ in range(n):
        fib.append(a)
        a, b = b, a + b  # Update Fibonacci numbers iteratively
    
    return fib

# Example usage
n = 1000
fib_numbers = efficient_fibonacci(n)

