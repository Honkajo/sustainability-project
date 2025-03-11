import networkx as nx

def efficient_pagerank(G, alpha=0.85, max_iter=100):
    # Use NetworkX's built-in function to calculate PageRank
    pagerank = nx.pagerank(G, alpha=alpha, max_iter=max_iter)
    return pagerank

# Example usage
G = nx.erdos_renyi_graph(50, 0.5)
result = efficient_pagerank(G)

