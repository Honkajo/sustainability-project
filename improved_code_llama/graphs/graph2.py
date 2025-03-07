import networkx as nx
import itertools

def graph_is_balanced(G):
    G1 = G.copy()
    G1.remove_edges_from([(u,v) for u,v,d in G1.edges(data=True) if d['weight'] == -1])
    con_comp = list(nx.connected_components(G1))
    if len(con_comp) > 1:
        return False
    for comp in con_comp:
        start_node = next(iter(comp))
        if not breadth_balance_check(G1, start_node):
            return False
    return True

def breadth_balance_check(G, start_node):
    queue = deque([(start_node, 0)])
    visited = {start_node: 0}
    level_nodes = {}

    while queue:
        node, depth = queue.popleft()

        if depth not in level_nodes:
            level_nodes[depth] = set()
        level_nodes[depth].add(node)
        

        for neigh in G.neighbors(node):
            if neigh not in visited:
                visited[neigh] = depth + 1
                queue.append((neigh, depth +1))
        
        for depth, nodes in level_nodes.items():
            for u,v in itertools.combinations(nodes, 2):
                if G.has_edge(u,v) and G[u][v].get('weight') == -1:
                    return False
    return True

def get_groups(G):
    start = next(iter(G.nodes))
    group1 = set()
    group1.add(start)
    group2 = set()
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()

        if node not in visited:
           visited.add(node)
        for neighbor in G.neighbors(node):
            if neighbor not in visited:
                queue.append(neighbor)
            if node in group1:
                if G[node][neighbor].get('weight') == -1:
                    group2.add(neighbor)
                else:
                    group1.add(neighbor)
            if node in group2:
                if G[node][neighbor].get('weight') == 1:
                    group2.add(neighbor)
                else:
                    group1.add(neighbor)
    return group1, group2

def bad_cycle(G):
    for cycle in nx.cycle_basis(G):
        length = len(cycle)
        counter = 0
        for idx, edge in enumerate(cycle):
            if idx == length-1:
                n1 = edge
                n2 = cycle[0]
            else:
                n1 = edge
                n2 = cycle[idx+1]
            if G[n1][n2].get('weight') == -1:
                counter += 1
        if counter % 2 != 0:
            return cycle

G1 = nx.Graph()
G2 = nx.Graph()

# Add edges with positive (+1) and negative (-1) weights
G1.add_edges_from([
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
])

G2.add_edges_from([
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
])

graph_is_balanced(G1)
graph_is_balanced(G2)
get_groups(G2)
bad_cycle(G1)

