import networkx as nx

def efficient_betweenness(G):
    # Use NetworkX's built-in function to calculate betweenness centrality
    betweenness = nx.betweenness_centrality(G)
    return betweenness

# Example usage
G = nx.erdos_renyi_graph(150, 0.5)
result = efficient_betweenness(G)

