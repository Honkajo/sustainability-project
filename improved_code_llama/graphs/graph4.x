import networkx as nx

def all_cycles(G):
    cycles = []
    for n in nx.simple_cycles(G):
        cycles.append(n)
    return cycles

# Example usage:
G = nx.erdos_renyi_graph(50, 0.5)  # Example graph with 50 nodes and 50% edge probability
result = all_cycles(G)

