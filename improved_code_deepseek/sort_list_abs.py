import random

random.seed(0)
L_size = 2000000  # int to pass to range

# Generate the list using list comprehension
L = [random.random() for _ in range(L_size)]

# Sort the list by absolute value in descending order
newL = sorted(L, key=abs, reverse=True)

