import random

random.seed(0)
L_size = 2000000  # Size of the list
L = [random.random() for _ in range(L_size)]

# Sort the list in descending order of absolute values
newL = sorted(L, key=abs, reverse=True)

