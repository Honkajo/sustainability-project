import networkx as nx
import random

def this_func(G, alpha=0.85, max_iter=100):
    # Initialize pagerank values for each node
    nodes = list(G.nodes())
    pagerank = {node: 1 / len(nodes) for node in nodes}  # Initialize all pageranks to 1/nodes
    
    # Iterate for a maximum number of iterations
    for _ in range(max_iter):
        new_pagerank = pagerank.copy()  # Make a copy to store updated values
        
        # Update the pagerank for each node based on neighbors
        for node in nodes:
            rank_sum = 0
            for neighbor in G.neighbors(node):
                # Add the contribution of each neighbor
                rank_sum += pagerank[neighbor] / len(list(G.neighbors(neighbor)))  # Outdegree of neighbor
                
            # Apply the PageRank formula
            new_pagerank[node] = (1 - alpha) / len(nodes) + alpha * rank_sum
        
        pagerank = new_pagerank  # Update the pagerank values

    return pagerank


# Example usage:
G = nx.erdos_renyi_graph(50, 0.5)  # Example graph with 50 nodes and 50% edge probability
result = this_func(G)

