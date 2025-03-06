import random
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

n = 500  # Number of nodes
probs = [1 / ((i + 1) * 10) for i in range(20)]  # List of probabilities
all_graphs = [[nx.gnp_random_graph(n, p) for _ in range(20)] for p in probs]

connect_probs = []
nodes_in_largest_components = []

# Calculate connectedness and largest component size for each probability
for graphs in all_graphs:
    connected_count = 0
    avg_largest_size = 0
    for G in graphs:
        connected_components = nx.connected_components(G)
        largest_component = max(connected_components, key=len)
        avg_largest_size += len(largest_component)
        if nx.is_connected(G):
            connected_count += 1

    connect_probs.append(connected_count / 20)  # Empirical relative frequency of connectivity
    nodes_in_largest_components.append(avg_largest_size / 20)  # Empirical average size of largest component



