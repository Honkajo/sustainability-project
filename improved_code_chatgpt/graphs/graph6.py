import networkx as nx

def this_func(G):
    # Compute betweenness centrality using NetworkX's efficient method
    betweenness = nx.betweenness_centrality(G, normalized=False)
    return betweenness

# Example usage:
G = nx.erdos_renyi_graph(150, 0.5)
result = this_func(G)

