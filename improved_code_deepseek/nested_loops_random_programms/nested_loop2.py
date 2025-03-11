import numpy as np

# Use NumPy to create the list efficiently
j_values = np.arange(100)
k_values = np.arange(1000)
l_values = np.arange(500)

# Create a meshgrid for j and k
j_grid, k_grid = np.meshgrid(j_values, k_values, indexing='ij')

# Filter based on the condition j < k
mask = j_grid < k_grid

# Calculate the number of valid (j, k) pairs
valid_pairs = np.sum(mask)

# Create the final list using broadcasting
listerator = np.tile(l_values, valid_pairs).tolist()

