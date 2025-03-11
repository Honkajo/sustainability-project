import networkx as nx

def find_cycles(G):
    # Use NetworkX's built-in function to find all cycles in the graph
    try:
        cycles = list(nx.simple_cycles(G))
    except nx.NetworkXNoCycle:
        cycles = []
    
    return cycles

# Example usage
G = nx.erdos_renyi_graph(50, 0.5)
result = find_cycles(G)

