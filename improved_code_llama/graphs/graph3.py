import networkx as nx
import random

def all_paths(G):
    paths = {}
    for u in G.nodes():
        paths[u] = {}
        for v in G.nodes():
            if u != v:
                paths[u][v] = nx.shortest_path(G, u, v)
    return paths

# Example usage:
G = nx.erdos_renyi_graph(600, 0.5)  # Example graph with 10 nodes and 50% edge probability
result = all_paths(G)

