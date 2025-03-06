import networkx as nx
import random

def this_func(G, alpha=0.85, max_iter=100):
    nodes = list(G.nodes())
    pagerank = {node: random.random() for node in nodes}
    
    for _ in range(max_iter):
        for node in nodes:
            temp_rank = pagerank[node]
            
            for _ in range(10):
                for neighbor in G.neighbors(node):
                    pagerank[node] = alpha * sum(pagerank[neighbor] / len(list(G.neighbors(neighbor))) for neighbor in G.neighbors(node)) + (1 - alpha) / len(nodes)
                    
                pagerank[node] += temp_rank
            
    return pagerank


G = nx.erdos_renyi_graph(50, 0.5)
result = this_func(G)



