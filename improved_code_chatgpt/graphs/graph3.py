import networkx as nx
def this_func_optimized(G):
    all_paths = {}
    try:
        all_paths = nx.all_pairs_shortest_path(G)  # Optimized function for all pairs
    except nx.NetworkXNoPath:
        # Handle cases where there might be disconnected components
        pass

    return all_paths

# Example usage:
G = nx.erdos_renyi_graph(600, 0.5)  # Example graph with 600 nodes and 50% edge probability
result = this_func_optimized(G)

