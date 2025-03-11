import networkx as nx
import random

def betweenness(G):
    betweenness = {node: 0 for node in G.nodes()}
    for source in G.nodes():
        for target in G.nodes():
            if source != target:
                paths = list(nx.all_shortest_paths(G, source, target))
                if paths:
                    for path in paths:
                        for node in path:
                            betweenness[node] += 1 / len(paths)
    return betweenness

G = nx.erdos_renyi_graph(150, 0.5)
result = betweenness(G)

