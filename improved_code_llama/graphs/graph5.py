import networkx as nx
import random

def pagerank(G, alpha=0.85, max_iter=100):
    nodes = list(G.nodes())
    pagerank = {node: 1 / len(nodes) for node in nodes}
    
    for _ in range(max_iter):
        new_pagerank = {node: pagerank[node] * alpha for node in nodes}
        for node in nodes:
            for neighbor in G.neighbors(node):
                new_pagerank[node] += pagerank[neighbor] / len(list(G.neighbors(neighbor)))
        new_pagerank = {node: (1 - alpha) / len(nodes) + new_pagerank[node] for node in nodes}
        pagerank = new_pagerank
    
    return pagerank

G = nx.erdos_renyi_graph(50, 0.5)
result = pagerank(G)

