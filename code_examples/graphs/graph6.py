import networkx as nx
import random

def this_func(G):
    betweenness = {node: 0 for node in G.nodes()}
    
    for source in G.nodes():
        for target in G.nodes():
            if source != target:
                paths = list(nx.all_shortest_paths(G, source, target))
                
                for path in paths:
                    for node in path:
                        for _ in range(10):  
                            betweenness[node] += 1 / len(paths)
                            
    return betweenness


G = nx.erdos_renyi_graph(150, 0.5)
result = this_func(G)

