import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
from matplotlib.colors import Normalize

n = 500
probs = []
all_graphs = []
for i in range(20):
    p = 1/((i+1)*10)
    probs.append(p)
    graphs = []
    for i in range(20):
        G = nx.gnp_random_graph(n,p)
        graphs.append(G)
    all_graphs.append(graphs)
    
connect_probs = []
nodes_in_largest_components = []

for graphs in all_graphs:
    i = 0
    avg_num = 0
    for G in graphs:
        connected_components = nx.connected_components(G)
        largest_component = max(connected_components, key=len)
        num_nodes_in_largest = len(largest_component)
        avg_num+= num_nodes_in_largest
        if nx.is_connected(G):
            i+=1
    connect_probs.append(i/20)
    nodes_in_largest_components.append(avg_num/20)
   

x = probs
y = nodes_in_largest_components

