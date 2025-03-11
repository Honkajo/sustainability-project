import numpy as np

# Use NumPy to create a grid of indices
i, j = np.mgrid[0:5000, 0:5000]

# Stack the indices into a single array of tuples
listerator = np.column_stack((i.ravel(), j.ravel()))

# Convert to a list of tuples (if needed)
listerator = [tuple(x) for x in listerator]

