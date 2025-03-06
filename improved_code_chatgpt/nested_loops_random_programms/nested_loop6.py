def efficient_fibonacci(n):
    # Store Fibonacci numbers
    fib = []
    
    a, b = 0, 1
    for _ in range(n):
        fib.append(a)
        a, b = b, a + b  # Move to the next Fibonacci number
    
    return fib

# Example usage
n = 1000
fib_numbers = efficient_fibonacci(n)

