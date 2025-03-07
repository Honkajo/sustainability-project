import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
from matplotlib.colors import Normalize

# Parameters
n = 500
num_p = 20
num_repetitions = 20  # Reduced from 20 to 10 for efficiency

# Precompute connection probabilities
probs = [1 / ((i + 1) * 10) for i in range(num_p)]

# Initialize data structures
all_graphs = [[] for _ in range(num_p)]  # Preallocate lists

# Generate graphs
for i in range(num_p):
    p = probs[i]
    for _ in range(num_repetitions):
        G = nx.gnp_random_graph(n, p)
        all_graphs[i].append(G)

# Analyze graphs
connect_probs = []
nodes_in_largest_components = []

for graphs in all_graphs:
    avg_num = 0
    connect_count = 0
    for G in graphs:
        if nx.is_connected(G):
            connect_count += 1
            avg_num += n
        else:
            # Find largest component only if not connected
            largest_component = max(nx.connected_components(G), key=len)
            avg_num += len(largest_component)
    connect_probs.append(connect_count / num_repetitions)
    nodes_in_largest_components.append(avg_num / num_repetitions)

# Optional: Convert to numpy arrays for efficient processing
connect_probs = np.array(connect_probs)
nodes_in_largest_components = np.array(nodes_in_largest_components)

x = probs
y = nodes_in_largest_components

