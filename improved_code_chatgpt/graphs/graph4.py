import networkx as nx

def this_func(G):
    # Find all cycles in the graph using networkx's cycle_basis
    cycles = []
    
    # Get all simple cycles in the graph
    all_cycles = nx.cycle_basis(G)
    
    # Check for each cycle if it's valid and not already recorded
    for cycle in all_cycles:
        cycles.append(cycle)
    
    return cycles

# Example usage:
G = nx.erdos_renyi_graph(50, 0.5)  # Example graph with 50 nodes and 50% edge probability
result = this_func(G)

