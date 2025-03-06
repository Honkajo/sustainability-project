import networkx as nx
import random

def this_func(G):
    nodes = list(G.nodes())
    all_paths = {}

    for i in range(len(nodes)):
        for j in range(len(nodes)):
            start_node = nodes[i]
            end_node = nodes[j]


            path = []

 
            for _ in range(len(G.nodes())):  
                if nx.has_path(G, start_node, end_node):
 
                    path = nx.shortest_path(G, source=start_node, target=end_node)
                    break

            
            if start_node not in all_paths:
                all_paths[start_node] = {}
            all_paths[start_node][end_node] = path

           
            if start_node != end_node:
                all_paths[start_node][end_node].append(path)

    return all_paths


# Example usage:
G = nx.erdos_renyi_graph(600, 0.5)  # Example graph with 10 nodes and 50% edge probability
result = this_func(G)

