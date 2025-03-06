def inefficient_fibonacci(n):
    # Store Fibonacci numbers
    fib = []
    
    # Outer loop to calculate Fibonacci up to 'n'
    for i in range(n):
        # Set the first two Fibonacci numbers
        a, b = 0, 1
        
        # Inner nested loop that unnecessarily recalculates Fibonacci numbers
        for j in range(i):
            for k in range(j):
                # Inefficient check (should just be calculating Fibonacci normally)
                if k == 0:
                    a, b = 0, 1  # Fibonacci base case
                else:
                    a, b = b, a + b  # Fibonacci recursive relation
        
        # Add the computed Fibonacci number to the list (unnecessary list operations)
        fib.append(a)
        
        # Extra inefficient checks (completely unnecessary)
        if i % 2 == 0:
            fib.append(b)
    
    return fib

# Example usage
n = 1000
fib_numbers = inefficient_fibonacci(n)
print(fib_numbers)

