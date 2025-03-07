import networkx as nx
import itertools
from collections import deque
import numpy as np

# Create sample graphs G1 and G2 with edges
G1 = nx.Graph()
G2 = nx.Graph()

# Add edges to G1
edges_G1 = [
    (1, 2, {'weight': 1}),
    (1, 3, {'weight': 1}),
    (2, 3, {'weight': 1}),
    (2, 4, {'weight': -1}),
    (2, 5, {'weight': 1}),
    (3, 6, {'weight': -1}),
    (4, 7, {'weight': -1}),
    (4, 9, {'weight': -1}),
    (5, 6, {'weight': -1}),
    (6, 8, {'weight': 1}),
    (6, 11, {'weight': -1}),
    (7, 12, {'weight': 1}),
    (8, 11, {'weight': -1}),
    (9, 12, {'weight': 1}),
    (10, 11, {'weight': -1}),
    (10, 12, {'weight': 1}),
    (11, 13, {'weight': -1}),
    (11, 14, {'weight': -1}),
    (12, 13, {'weight': 1}),
    (13, 15, {'weight': -1}),
    (14, 15, {'weight': -1}),
]
G1.add_edges_from(edges_G1)

# Add edges to G2 (simplified for demonstration)
edges_G2 = [
    (1, 2, {'weight': 1}),
    (1, 3, {'weight': 1}),
    (2, 3, {'weight': 1}),
    (2, 4, {'weight': 1}),
    (2, 5, {'weight': 1}),
    (3, 6, {'weight': -1}),
    (4, 7, {'weight': -1}),
    (4, 9, {'weight': -1}),
    (5, 6, {'weight': -1}),
    (6, 8, {'weight': 1}),
    (6, 11, {'weight': -1}),
    (7, 12, {'weight': 1}),
    (8, 11, {'weight': -1}),
    (9, 12, {'weight': 1}),
    (10, 11, {'weight': -1}),
    (10, 12, {'weight': 1}),
    (11, 13, {'weight': -1}),
    (11, 14, {'weight': -1}),
    (12, 13, {'weight': 1}),
    (13, 15, {'weight': -1}),
    (14, 15, {'weight': -1}),
]
G2.add_edges_from(edges_G2)

def get_isolated_nodes(G):
    """Return isolated nodes in the graph."""
    isolated = [node for node in G.nodes if G.degree(node) == 0]
    return isolated

def has_neg_connection(G, components):
    """Check if any component has a negative connection."""
    for comp in components:
        for u, v in itertools.combinations(comp, 2):
            if G.has_edge(u, v) and G[u][v].get('weight') == -1:
                return True
    return False

def connected_con_comp_graph(G, components):
    """Construct a graph where nodes are connected components."""
    component_graph = nx.Graph()
    component_map = {}
    
    for i, comp in enumerate(components):
        component_map[frozenset(comp)] = i
        component_graph.add_node(i)
    
    for comp1, comp2 in itertools.combinations(components, 2):
        for u, v in itertools.product(comp1, comp2):
            if G.has_edge(u, v):
                component_graph.add_edge(component_map[frozenset(comp1)], component_map[frozenset(comp2)])
                break
    return component_graph

def breadth_balance_check(G, start_node):
    """Check if the graph is balanced using BFS."""
    visited = {start_node}
    queue = deque([start_node])
    level_nodes = {0: {start_node}}
    
    while queue:
        node = queue.popleft()
        current_level = len(level_nodes)
        
        for neighbor in G.neighbors(node):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                level_nodes.setdefault(current_level + 1, set()).add(neighbor)
        
        for level in level_nodes.values():
            for u, v in itertools.combinations(level, 2):
                if G.has_edge(u, v):
                    return False
    return True

def graph_is_balanced(G):
    """Check if the graph is balanced."""
    # Create a subgraph with only positive edges
    positive_edges = [(u, v) for u, v, data in G.edges(data=True) if data['weight'] == 1]
    positive_subgraph = nx.Graph()
    positive_subgraph.add_edges_from(positive_edges)
    
    # Find connected components in the positive subgraph
    components = list(nx.connected_components(positive_subgraph))
    
    # Check for negative connections within components
    if has_neg_connection(G, components):
        return False
    
    # Add isolated nodes as single-node components
    isolated_nodes = get_isolated_nodes(G)
    components += [{node} for node in isolated_nodes]
    
    # Construct component connection graph
    component_graph = connected_con_comp_graph(G, components)
    
    # Check balance for each component in the component graph
    for component in nx.connected_components(component_graph):
        start_node = next(iter(component))
        if not breadth_balance_check(component_graph, start_node):
            return False
    return True

def get_groups(G):
    """Divide nodes into two groups based on edge weights."""
    if not G:
        return set(), set()
    
    start_node = next(iter(G.nodes))
    group1 = {start_node}
    group2 = set()
    visited = set()
    queue = deque([start_node])
    visited.add(start_node)
    
    while queue:
        node = queue.popleft()
        
        for neighbor in G.neighbors(node):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                if G[node][neighbor]['weight'] == -1:
                    if node in group1:
                        group2.add(neighbor)
                    else:
                        group1.add(neighbor)
                else:
                    if node in group1:
                        group1.add(neighbor)
                    else:
                        group2.add(neighbor)
    
    return group1, group2

def bad_cycle(G):
    """Find a cycle with an odd number of negative edges."""
    cycles = nx.cycle_basis(G)
    for cycle in cycles:
        negative_edges = 0
        for i in range(len(cycle)):
            u = cycle[i]
            v = cycle[(i + 1) % len(cycle)]
            if G[u][v].get('weight') == -1:
                negative_edges += 1
        if negative_edges % 2 != 0:
            return cycle
    return None

# Example usage
if __name__ == "__main__":
    # Check if graphs are balanced
    graph_is_balanced(G1)
    graph_is_balanced(G2)
    
    # Get groups for G2
    group1, group2 = get_groups(G2)

    
    # Find bad cycle in G1
    bad_cycle_result = bad_cycle(G1)


