import numpy as np
import networkx as nx

n = 500
probs = np.array([1/((i+1)*10) for i in range(20)])
all_graphs = [nx.gnp_random_graph(n,p) for p in probs for _ in range(20)]

connect_probs = []
nodes_in_largest_components = []

for i in range(len(probs)):
    num_connected = 0
    total_nodes = 0
    for G in all_graphs[i*20:(i+1)*20]:
        connected_components = nx.connected_components(G)
        largest_component = max(connected_components, key=len)
        num_nodes_in_largest = len(largest_component)
        total_nodes += num_nodes_in_largest
        if nx.is_connected(G):
            num_connected += 1
    connect_probs.append(num_connected/20)
    nodes_in_largest_components.append(total_nodes/20)

x = probs
y = nodes_in_largest_components

