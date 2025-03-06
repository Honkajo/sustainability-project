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
plt.figure(figsize=(40, 40))
plt.scatter(x, y, color='blue', alpha=1.0, s=200)
plt.title(f"Empirical Average Plot", fontsize=40)
plt.xlabel("Probability", fontsize=40)
plt.ylabel("Empirical Average", fontsize=40)
plt.figtext(0.5, 0.05,f"This is the scatterplot for the empircal average", 
            wrap=True, horizontalalignment='center', fontsize=30)
plt.grid(True)
#plt.savefig(f"Empircal Average.png", format="png") 

y = connect_probs
plt.figure(figsize=(40, 40))
plt.scatter(x, y, color='blue', alpha=1.0, s=200)
plt.title(f"Empirical Relative Frequency Plot", fontsize=40)
plt.xlabel("Probability", fontsize=40)
plt.ylabel("Empirical Relative Frequency", fontsize=40)
plt.figtext(0.5, 0.05,f"This is the scatterplot for the empircal relative frequency", 
            wrap=True, horizontalalignment='center', fontsize=30)
plt.grid(True)
#plt.savefig(f"Empircal Relative Frequency.png", format="png") 
