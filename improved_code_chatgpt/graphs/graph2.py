def get_isolated_nodes(G1, G2):
    # Get connected components of G1
    components = list(nx.connected_components(G1))  
    all_nodes = set(G2.nodes)  
    connected_nodes = set(node for comp in components for node in comp)  # All connected nodes
    isolated_nodes = all_nodes - connected_nodes  # Isolated nodes
    print("All nodes in G2:", all_nodes)
    print("Connected nodes in G1:", connected_nodes)
    
    # Add isolated nodes to components as single-node sets
    for node in isolated_nodes:
        components.append({node})
    
    return components

