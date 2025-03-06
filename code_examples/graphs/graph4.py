import networkx as nx

def this_func(G):
    cycles = []
    nodes = list(G.nodes())
    
    for i in range(len(nodes)):
        for j in range(i, len(nodes)):
            for k in range(j, len(nodes)):
                for l in range(k, len(nodes)):
                    subgraph = G.subgraph([nodes[i], nodes[j], nodes[k], nodes[l]])
                    if nx.is_connected(subgraph):
                        try:
                            cycle = nx.find_cycle(subgraph)
                            cycles.append(cycle)
                        except nx.NetworkXNoCycle:
                            pass
    
    return cycles


G = nx.erdos_renyi_graph(50, 0.5)
result = this_func(G)
